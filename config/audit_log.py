from config.db_config import get_connection
from datetime import datetime

def log_action(action, certificate, table_name, status, patient_id=None):
    conn   = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO Audit_Log 
           (timestamp, action, certificate, table_name, status, patient_id)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            action,
            certificate,
            table_name,
            status,
            patient_id
        )
    )

    conn.commit()
    cursor.close()
    conn.close()