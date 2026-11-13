
from database import get_connection

class Student:

    @staticmethod
    def add_student():

        print("\n--- Add New Student ---")

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Student name cannot be empty!")
            return

        try:
            age = int(input("Enter Student Age: "))

            if age <= 0 or age > 100:
                print("Enter a valid age!")
                return

        except ValueError:
            print("Age must be a number!")
            return

        class_name = input("Enter Class Name: ").strip()

        if not class_name:
            print("Class name cannot be empty!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (name, age, class_name)
            VALUES (?, ?, ?)
        """, (name, age, class_name))

        connection.commit()

        print("\nStudent added successfully!")
        print("Student ID:", cursor.lastrowid)

        connection.close()

    @staticmethod
    def view_students():

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT student_id, name, age, class_name
            FROM students
            ORDER BY student_id
        """)

        students = cursor.fetchall()
        connection.close()

        print("\n--- Student List ---")

        if not students:
            print("No student records found!")
            return

        print("-" * 65)
        print(f"{'ID':<8}{'Name':<22}{'Age':<10}{'Class':<15}")
        print("-" * 65)

        for student in students:
            print(
                f"{student[0]:<8}"
                f"{student[1]:<22}"
                f"{student[2]:<10}"
                f"{student[3]:<15}"
            )

        print("-" * 65)

    @staticmethod
    def search_student():

        print("\n--- Search Student ---")

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT student_id, name, age, class_name
            FROM students
            WHERE student_id = ?
        """, (student_id,))

        student = cursor.fetchone()
        connection.close()

        if student:
            print("\nStudent Found!")
            print("Student ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Class:", student[3])
        else:
            print("Student not found!")

    @staticmethod
    def delete_student():

        print("\n--- Delete Student ---")

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name FROM students
            WHERE student_id = ?
        """, (student_id,))

        student = cursor.fetchone()

        if not student:
            print("Student not found!")
            connection.close()
            return

        confirm = input(
            f"Delete {student[0]}? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            cursor.execute("""
                DELETE FROM students
                WHERE student_id = ?
            """, (student_id,))

            connection.commit()
            print("Student deleted successfully!")

        else:
            print("Delete operation cancelled!")

        connection.close()