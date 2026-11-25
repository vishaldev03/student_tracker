from database.connection import get_db_connection
from psycopg2 import Error

def add_marks():
    """Adds exam marks for a student."""
    print("\n--- Add Student Marks ---")
    
    try:
        student_id = int(input("Enter Student ID: ").strip())
        subject_id = int(input("Enter Subject ID: ").strip())
    except ValueError:
        print("❌ Error: ID must be an integer.")
        return

    exam_type = input("Enter exam type (e.g., Mid-Term, End-Term, Assignment): ").strip()
    if not exam_type:
        print("❌ Error: Exam type cannot be empty.")
        return

    try:
        score = float(input("Enter obtained score: ").strip())
        max_marks = input("Enter maximum marks [Default 100]: ").strip()
        max_marks = float(max_marks) if max_marks else 100.00
    except ValueError:
        print("❌ Error: Marks must be a valid number.")
        return

    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO marks (student_id, subject_id, exam_type, score, max_marks)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (student_id, subject_id, exam_type, score, max_marks))
        conn.commit()
        print(f"✅ Marks added successfully for Student ID {student_id}!")

    except Error as e:
        conn.rollback()
        print(f"❌ Database error (Verify Student ID and Subject ID): {e}")
    finally:
        cursor.close()
        conn.close()


def view_performance():
    """Displays student performance and marks records."""
    print("\n--- Performance Report ---")
    
    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT m.id, s.name, sub.subject_name, m.exam_type, m.score, m.max_marks
            FROM marks m
            JOIN student s ON m.student_id = s.id
            JOIN subject sub ON m.subject_id = sub.id
            ORDER BY s.name, sub.subject_name;
        """
        cursor.execute(query)
        records = cursor.fetchall()

        if not records:
            print("📭 No performance records available.")
            input("\n press enter to return to main manu ....")
            return

        print(f"{'id':<5} | {'student Name':<20} | {'subject':<20} | {'exam Type':<15} | {'score':<10} | {'max marks':<10}")
        print("-" * 90)
        for row in records:
            mark_id, student_name, subject_name, exam_type, score, max_marks = row
            print(f"{mark_id:<5} | {student_name:<20} | {subject_name:<20} | {exam_type:<15} | {score:<10} | {max_marks:<10}")

        input("\n press enter to return to main manu ....")
    except Error as e:
        print(f"❌ Error fetching data: {e}")
    finally:
        cursor.close()
        conn.close()