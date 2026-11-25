from database.connection import get_db_connection
from psycopg2 import Error

def add_subject():
    """Adds a new subject to the database."""
    print("\n--- Add New Subject ---")
    subject_name = input("Enter subject name: ").strip()
    code = input("Enter subject code (e.g., CS201): ").strip()

    if not subject_name or not code:
        print("❌ Error: All fields are required.")
        return

    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO subject (subject_name, code)
            VALUES (%s, %s);
        """
        cursor.execute(query, (subject_name, code))
        conn.commit()
        print(f"✅ subject '{subject_name}' ({code}) added successfully!")

    except Error as e:
        conn.rollback()
        print(f"❌ Database error (Subject code may already exist): {e}")
    finally:
        cursor.close()
        conn.close()


def view_subject():
    """Displays a list of all available subject."""
    print("\n--- All subject List ---")
    
    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, subject_name, code FROM subject ORDER BY id;")
        subject = cursor.fetchall()

        if not subject:
            print("📭 No subject registered in the database.")
            return

        print(f"{'id':<5} | {'subject Name':<25} | {'subject Code':<15}")
        print("-" * 50)
        for row in subject:
            sub_id, name, code = row
            print(f"{sub_id:<5} | {name:<25} | {code:<15}")

    except Error as e:
        print(f"❌ Error fetching data: {e}")
    finally:
        cursor.close()
        conn.close()