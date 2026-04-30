import sys
from config.cert_config import CA_CERT, CLIENT_CERT
from config.cert_verifier import verify_certificate
from database.fetch_pad import encrypt_pad, decrypt_pad, decrypt_pad_by_cnic
from database.fetch_pmd import encrypt_pmd, decrypt_pmd
from database.fetch_pfd import encrypt_pfd, decrypt_pfd

def print_header():
    print("\n" + "=" * 60)
    print("   ASHN Cryptography System")
    print("   PakSecure Cyber Solutions")
    print("=" * 60)
# ENCRYPTION
def encrypt_all():
    print("\n[PHASE 1] — CERTIFICATE VERIFICATION")
    verify_certificate(CA_CERT, CLIENT_CERT)

    print("\n[PHASE 2] — DATA ENCRYPTION")
    encrypt_pad()
    encrypt_pmd()
    encrypt_pfd()

    print("\n" + "=" * 60)
    print("   All Sensitive Data Encrypted in MySQL")
    print("=" * 60)
# DECRYPTION
def decrypt_all():
    print("\n[PHASE 1] — CERTIFICATE VERIFICATION")
    verify_certificate(CA_CERT, CLIENT_CERT)

    print("\n[PHASE 2] — DECRYPTING ALL DATA IN MYSQL")
    decrypt_pad(all_rows=True)
    decrypt_pmd(all_rows=True)
    decrypt_pfd(all_rows=True)

    print("\n" + "=" * 60)
    print("   All Sensitive Data Decrypted in MySQL")
    print("=" * 60)

def search_by_patient_id():
    patient_id = input("\n  Enter Patient ID: ").strip()

    if not patient_id.isdigit():
        print("\n  [✗] Invalid Patient ID — must be a number")
        return

    patient_id = int(patient_id)

    print("\n  Which data to decrypt?")
    print("  [1] Admin Data    (PAD)")
    print("  [2] Medical Data  (PMD)")
    print("  [3] Finance Data  (PFD)")
    print("  [4] All")
    choice = input("\n  Enter choice: ").strip()

    print("\n[PHASE 1] — CERTIFICATE VERIFICATION")
    verify_certificate(CA_CERT, CLIENT_CERT)

    print("\n[PHASE 2] — DECRYPTING PATIENT DATA")

    if choice == '1':
        decrypt_pad(patient_id=patient_id)
    elif choice == '2':
        decrypt_pmd(patient_id=patient_id)
    elif choice == '3':
        decrypt_pfd(patient_id=patient_id)
    elif choice == '4':
        decrypt_pad(patient_id=patient_id)
        decrypt_pmd(patient_id=patient_id)
        decrypt_pfd(patient_id=patient_id)
    else:
        print("\n  [✗] Invalid choice")

def search_by_cnic():
    cnic_input = input("\n  Enter CNIC (format: #####-#######-#): ").strip()

    print("\n  Which data to decrypt?")
    print("  [1] Admin Data    (PAD)")
    print("  [2] Medical Data  (PMD)")
    print("  [3] Finance Data  (PFD)")
    print("  [4] All")
    choice = input("\n  Enter choice: ").strip()

    print("\n[PHASE 1] — CERTIFICATE VERIFICATION")
    verify_certificate(CA_CERT, CLIENT_CERT)

    print("\n[PHASE 2] — SEARCHING BY CNIC")
    pad_rows = decrypt_pad_by_cnic(cnic_input=cnic_input)

    if pad_rows and choice in ['2', '3', '4']:
        for pid in pad_rows:
            if choice == '2':
                decrypt_pmd(patient_id=pid)
            elif choice == '3':
                decrypt_pfd(patient_id=pid)
            elif choice == '4':
                decrypt_pmd(patient_id=pid)
                decrypt_pfd(patient_id=pid)

def view_audit_log():
    from config.db_config import get_connection
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Audit_Log ORDER BY timestamp DESC LIMIT 20")
    logs = cursor.fetchall()

    print("\n" + "=" * 60)
    print("   AUDIT LOG — Last 20 Entries")
    print("=" * 60)
    print(f"\n  {'Timestamp':<22} {'Action':<15} {'Certificate':<25} {'Table':<25} {'Status':<10} {'Patient'}")
    print(f"  {'-'*22} {'-'*15} {'-'*25} {'-'*25} {'-'*10} {'-'*10}")

    for log in logs:
        patient = str(log['patient_id']) if log['patient_id'] else '—'
        print(f"  {str(log['timestamp']):<22} {log['action']:<15} {log['certificate']:<25} {log['table_name']:<25} {log['status']:<10} {patient}")

    cursor.close()
    conn.close()

def main_menu():
    print_header()

    while True:
        print("\n" + "-" * 60)
        print("  MAIN MENU")
        print("-" * 60)
        print("  [1] Encrypt All Data")
        print("  [2] Decrypt All Data")
        print("  [3] Search Patient by ID")
        print("  [4] Search Patient by CNIC")
        print("  [5] View Audit Log")
        print("  [6] Exit")
        print("-" * 60)

        choice = input("\n  Enter choice: ").strip()

        if choice == '1':
            encrypt_all()
        elif choice == '2':
            decrypt_all()
        elif choice == '3':
            search_by_patient_id()
        elif choice == '4':
            search_by_cnic()
        elif choice == '5':
            view_audit_log()
        elif choice == '6':
            print("\n  Exiting — PakSecure Cyber Solutions")
            print("=" * 60)
            sys.exit(0)
        else:
            print("\n  [✗] Invalid choice — please try again")

if __name__ == "__main__":
    main_menu()

