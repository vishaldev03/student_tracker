from datetime import datetime
from database.connection import get_db_connection
from psycopg2 import Error

def mark_attendance():
    """Records attendance (Present/Absent) for a student."""
    print("\n--- Mark Attendance ---")
    
    try:
        student_id = int(input("Enter student ID: ").strip())
        subject_id = int(input("Enter subject ID: ").strip())
    except ValueError:
        print("❌ Error: ID must be an integer.")
        return

    date_str = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')

    status_input = input("Enter status - (P)resent or (A)bsent: ").strip().upper()
    if status_input == 'P':
        status = 'Present'
    elif status_input == 'A':
        status = 'Absent'
    else:
        print("❌ Invalid choice! Enter only 'P' or 'A'.")
        return

    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO attendance (student_id, subject_id, date, status)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (student_id, subject_id, date_str, status))
        conn.commit()
        print(f"✅ attendance recorded as '{status}' for student id {student_id} on {date_str}!")

    except Error as e:
        conn.rollback()
        print(f"❌ Database error (Verify student id and subject id): {e}")
    finally:
        cursor.close()
        conn.close()


def view_attendance():
    """Displays attendance records."""
    print("\n--- Attendance Report ---")
    
    conn = get_db_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT a.id, s.name, sub.subject_name, a.date, a.status
            FROM attendance a
            JOIN student s ON a.student_id = s.id
            JOIN subject sub ON a.subject_id = sub.id
            ORDER BY a.date DESC, s.name;
        """
        cursor.execute(query)
        records = cursor.fetchall()

        if not records:
            print("📭 No attendance records available.")
            return

        print(f"{'id':<5} | {'student Name':<20} | {'subject':<20} | {'date':<12} | {'status':<10}")
        print("-" * 75)
        for row in records:
            att_id, student_name, subject_name, date, status = row
            print(f"{att_id:<5} | {student_name:<20} | {subject_name:<20} | {str(date):<12} | {status:<10}")

    except Error as e:
        print(f"❌ Error fetching data: {e}")
    finally:
        cursor.close()
        conn.close()