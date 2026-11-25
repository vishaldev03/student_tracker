import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Establishes a connection to the PostgreSQL database and returns the connection object."""
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def test_connection():
    """Tests the database connection."""
    conn = get_db_connection()
    if conn:
        print("✅ Successfully connected to the PostgreSQL database!")
        conn.close()

if __name__ == "_main_":
    test_connection()