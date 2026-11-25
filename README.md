# 🎓 Student Attendance & Performance Tracker

A modular, console-based backend application built with **Python** and **PostgreSQL** to streamline student record management, 
daily attendance tracking, and academic performance reporting.

---

## ✨ Key Features

- **🔐 Admin Authentication:** Secure login verification before accessing system operations.
- **👨‍🎓 Student Management:** Add new student records and view complete student directories.
- **📚 Subject Management:** Create and manage academic subjects seamlessly.
- **📅 Attendance Tracking:** Mark daily student attendance and generate detailed attendance reports.
- **📊 Performance Analytics:** Record student marks and view comprehensive academic performance reports.
- **🗄️ Relational Database Integration:** Powered by PostgreSQL with structured schema design and connection pooling via `psycopg2`.

---

## 🛠️ Tech Stack

- **Language:** Python language
- **Database:** PostgreSQL
- **Database Adapter:** `psycopg2`
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
student_tracker/
│
├── database/
│   ├── __init__.py
│   ├── connection.py      # PostgreSQL database connection setup
│   └── schema.sql         # SQL table definitions
│
├── modules/
│   ├── __init__.py
│   ├── auth.py            # Admin login authentication
│   ├── student.py         # Student CRUD operations
│   ├── subject.py         # Subject management logic
│   ├── attendance.py      # Attendance marking & reporting
│   └── performance.py     # Marks entry & performance reports
│
├── .gitignore             # Excludes .env and cache files
├── main.py                # Application entry point & console menu
└── requirements.txt       # Project dependencies
