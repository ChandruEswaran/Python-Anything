
import sqlite3

DATABASE_NAME = "students.db"


def get_connection():
    """Create and return a database connection."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # Student details table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            class_name TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Student marks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            marks REAL NOT NULL,
            max_marks REAL NOT NULL,
            UNIQUE(student_id, subject),
            FOREIGN KEY(student_id)
                REFERENCES students(student_id)
                ON DELETE CASCADE
        )
    """)

    connection.commit()
    connection.close()

    print("Database and tables created successfully!")
