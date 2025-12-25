import mysql.connector
from .config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    print("Connected Database:", cursor.fetchone())
    cursor.close()
    conn.close()
