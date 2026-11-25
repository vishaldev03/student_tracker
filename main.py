from modules.student import add_student, view_student
from modules.subject import add_subject, view_subject
from modules.attendance import mark_attendance, view_attendance
from modules.performance import add_marks, view_performance
from modules.auth import admin_login

def main_menu():
    """Main menu loop displaying console options."""
    while True:
        print("\n==============================================")
        print("     📚 STUDENT ATTENDANCE & PERFORMANCE      ")
        print("==============================================")
        print("1. Add New Student")
        print("2. View All Student")
        print("3. Add New Subject")
        print("4. View All Subject")
        print("5. Mark Attendance")
        print("6. View Attendance Report")
        print("7. Add Student Marks")
        print("8. View Performance Report")
        print("9. Exit")
        print("==============================================")
        
        choice = input("Choose an option (1-9): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            add_subject()
        elif choice == '4':
            view_subject()
        elif choice == '5':
            mark_attendance()
        elif choice == '6':
            view_attendance()
        elif choice == '7':
            add_marks()
        elif choice == '8':
            view_performance()
        elif choice == '9':
            print("\n🙏 Exiting program. Thank you!")
            break
        else:
            print("❌ Invalid option! Please choose a number between 1 and 9.")

if __name__ == "__main__":
    if admin_login():
        main_menu()