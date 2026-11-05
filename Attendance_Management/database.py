import sqlite3
import os


# Database directory
DATABASE_FOLDER = "database"

# Database file path
DATABASE_NAME = os.path.join(
    DATABASE_FOLDER,
    "attendance.db"
)


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    # Enable foreign key constraints
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def create_tables():

    # Create database folder if not available
    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    connection = get_connection()
    cursor = connection.cursor()

    # Members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (

            member_id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            age INTEGER NOT NULL,

            department TEXT NOT NULL,

            phone TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # Attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (

            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,

            member_id INTEGER NOT NULL,

            attendance_date TEXT NOT NULL,

            status TEXT NOT NULL
                CHECK(status IN ('P', 'A', 'L')),

            remarks TEXT,

            UNIQUE(member_id, attendance_date),

            FOREIGN KEY(member_id)
                REFERENCES members(member_id)
                ON DELETE CASCADE

        )
    """)

    connection.commit()
    connection.close()

    print("Database and tables created successfully!")
