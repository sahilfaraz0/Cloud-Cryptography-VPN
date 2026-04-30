import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="10.8.0.1",
        user="root",
        password="12345678",
        database="ashn_db"
    )
    return conn