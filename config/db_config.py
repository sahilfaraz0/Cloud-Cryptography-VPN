import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="ashn_db"
    )
    return conn