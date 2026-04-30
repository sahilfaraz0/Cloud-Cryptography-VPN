from config.db_config import get_connection
from encryption.aesgcm_encrypt import encrypt_aes_gcm, decrypt_aes_gcm
from encryption.hashing import hash_value, verify_hash
from config.audit_log import log_action

SENSITIVE_COLUMNS = [
    'total_amount_pkr', 'insurance_details', 'billing_notes',
    'invoice_description', 'bank_account_number', 'tax_id'
]


def encrypt_pfd():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Patient_Finance_Data")
    rows = cursor.fetchall()

    print("\n" + "=" * 60)
    print("   ENCRYPTING — Patient Finance Data (AES-GCM)")
    print("=" * 60)

    update_data = []
    key_data = []
    hash_data = []

    for row in rows:
        for col in SENSITIVE_COLUMNS:
            original = str(row[col]) if row[col] is not None else None
            if original is None:
                continue

            col_hash = hash_value(original)
            encrypted = encrypt_aes_gcm(original)

            update_data.append((encrypted['ciphertext'], row['finance_id'], col))
            key_data.append(('Patient_Finance_Data', row['finance_id'], col, 'AES-GCM',
                             encrypted['key'], encrypted['nonce'], encrypted['tag']))
            hash_data.append(('Patient_Finance_Data', row['finance_id'], col, col_hash))

    update_cursor = conn.cursor()
    for col in SENSITIVE_COLUMNS:
        col_updates = [(d[0], d[1]) for d in update_data if d[2] == col]
        if col_updates:
            update_cursor.executemany(
                f"UPDATE Patient_Finance_Data SET {col} = %s WHERE finance_id = %s",
                col_updates
            )

    update_cursor.executemany(
        """INSERT INTO Encryption_Keys
               (table_name, row_id, column_name, algo, enc_key, nonce, tag)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        key_data
    )
    update_cursor.executemany(
        """INSERT INTO Data_Hashes
               (table_name, row_id, column_name, hash_value)
           VALUES (%s, %s, %s, %s)""",
        hash_data
    )

    state_data = [('Patient_Finance_Data', int(row['patient_id']), True) for row in rows if 'patient_id' in row]
    if state_data:
        update_cursor.executemany(
            """INSERT INTO Encryption_State (table_name, patient_id, is_encrypted)
               VALUES (%s, %s, %s) ON DUPLICATE KEY
            UPDATE is_encrypted =
            VALUES (is_encrypted)""",
            state_data
        )

    conn.commit()
    log_action('ENCRYPT', 'SYSTEM', 'Patient_Finance_Data', 'SUCCESS')
    update_cursor.close()

    cursor.execute("SELECT * FROM Patient_Finance_Data LIMIT 1")
    sample = cursor.fetchone()

    if sample:
        print(f"\n  Encrypted Columns : {', '.join(SENSITIVE_COLUMNS)}")
        print(f"  Total Rows        : {len(rows)}")
        print(f"  Status            : Complete ✓")
        print(f"\n  Sample — Finance ID: {sample['finance_id']}")
        print(f"  -------------------------")
        for col in SENSITIVE_COLUMNS:
            print(f"  {col:<25} ENCRYPTED : {str(sample[col])[:40]}...")

    cursor.close()
    conn.close()


def decrypt_pfd(patient_id=None, all_rows=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if patient_id:
        cursor.execute("SELECT * FROM Patient_Finance_Data WHERE patient_id = %s", (patient_id,))
    elif all_rows:
        cursor.execute("SELECT * FROM Patient_Finance_Data")
    else:
        cursor.execute("SELECT * FROM Patient_Finance_Data LIMIT 1")

    rows = cursor.fetchall()

    if not rows:
        if patient_id:
            print(f"\n  [!] No records found for Patient ID: {patient_id} in Patient_Finance_Data.")
        return

    key_cursor = conn.cursor(dictionary=True)
    key_cursor.execute("SELECT * FROM Encryption_Keys WHERE table_name = 'Patient_Finance_Data'")
    all_keys = key_cursor.fetchall()

    key_cursor.execute("SELECT * FROM Data_Hashes WHERE table_name = 'Patient_Finance_Data'")
    all_hashes = key_cursor.fetchall()

    key_cursor.execute(
        "SELECT patient_id, is_encrypted FROM Encryption_State WHERE table_name = 'Patient_Finance_Data'")
    states = {int(s['patient_id']): s['is_encrypted'] for s in key_cursor.fetchall()}
    key_cursor.close()

    key_index = {(int(k['row_id']), k['column_name']): k for k in all_keys}
    hash_index = {(int(h['row_id']), h['column_name']): h for h in all_hashes}

    print("\n" + "=" * 60)
    print("   DECRYPTING — Patient Finance Data (AES-GCM)")
    print("=" * 60)

    update_data = []
    sample_printed = False
    print_all = bool(patient_id)

    for row in rows:
        fid = int(row['finance_id'])
        pid = int(row['patient_id'])
        is_encrypted = states.get(pid, False)

        if not is_encrypted:
            if print_all or not sample_printed:
                print(f"\n  Finance ID : {fid}")
                print(f"  Patient ID : {pid}")
                print(f"  -------------------------")
                for col in SENSITIVE_COLUMNS:
                    print(f"  {col:<25} : {row.get(col, '')}")
                print(f"\n  [!] Data is currently unencrypted in the database.")
                sample_printed = True
            continue

        col_results = {}
        all_verified = True
        for col in SENSITIVE_COLUMNS:
            key_row = key_index.get((fid, col))
            hash_row = hash_index.get((fid, col))

            if key_row is None:
                continue

            encrypted = {
                "key": key_row['enc_key'],
                "nonce": key_row['nonce'],
                "tag": key_row['tag'],
                "ciphertext": row[col]
            }

            decrypted = decrypt_aes_gcm(encrypted)
            update_data.append((decrypted, fid, col))

            if hash_row and not verify_hash(decrypted, hash_row['hash_value']):
                all_verified = False

            col_results[col] = decrypted

        if col_results and (print_all or not sample_printed):
            print(f"\n  Finance ID : {fid}")
            print(f"  Patient ID : {pid}")
            print(f"  -------------------------")
            for col, val in col_results.items():
                print(f"  {col:<25} : {val}")
            if all_verified:
                print(f"\n  [✓] Integrity Verified — All columns intact")
            else:
                print(f"\n  [✗] INTEGRITY FAILED — Data may have been tampered")
            sample_printed = True

    update_cursor = conn.cursor()
    if all_rows:
        for col in SENSITIVE_COLUMNS:
            col_updates = [(d[0], d[1]) for d in update_data if d[2] == col]
            if col_updates:
                update_cursor.executemany(
                    f"UPDATE Patient_Finance_Data SET {col} = %s WHERE finance_id = %s",
                    col_updates
                )

        state_updates = [('Patient_Finance_Data', int(row['patient_id']), False) for row in rows if 'patient_id' in row]
        if state_updates:
            update_cursor.executemany(
                """INSERT INTO Encryption_State (table_name, patient_id, is_encrypted)
                   VALUES (%s, %s, %s) ON DUPLICATE KEY
                UPDATE is_encrypted =
                VALUES (is_encrypted)""",
                state_updates
            )

    conn.commit()
    log_action('DECRYPT', 'karachi.ashn.pk', 'Patient_Finance_Data', 'SUCCESS',
               patient_id if patient_id else None)
    update_cursor.close()

    if all_rows:
        print(f"\n  Total Rows Decrypted : {len(rows)}")

    cursor.close()
    conn.close()
    