from database.connection import get_db_connection
from psycopg2 import Error

def add_student():
    """Adds a new student to the database."""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    email = input("Enter email address: ").strip()
    enrollment_no = input("Enter enrollment number: ").strip()
    
    try:
        semester = int(input("Enter semester (e.g., 1, 2, 3...): ").strip())
    except ValueError:
        print("❌ Error: Semester must be a valid integer.")
        return

    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO student (name, email, enrollment_no, semester)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (name, email, enrollment_no, semester))
        conn.commit()
        print(f"✅ student '{name}' added successfully!")

    except Error as e:
        conn.rollback()
        print(f"❌ Database error (email or enrollment number may already exist): {e}")
    finally:
        cursor.close()
        conn.close()


def view_student():
    """Displays a list of all registered student."""
    print("\n--- All Student List ---")
    
    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, enrollment_no, semester, created_at FROM student ORDER BY id;")
        student = cursor.fetchall()

        if not student:
            print("📭 No students registered in the database.")
            return

        print(f"{'ID':<5} | {'name':<20} | {'email':<25} | {'enrollment No':<15} | {'semester':<10}")
        print("-" * 85)
        for row in student:
            student_id, name, email, enrollment_no, semester, _ = row
            print(f"{student_id:<5} | {name:<20} | {email:<25} | {enrollment_no:<15} | {semester:<10}")

    except Error as e:
        print(f"❌ Error fetching data: {e}")
    finally:
        cursor.close()
        conn.close()