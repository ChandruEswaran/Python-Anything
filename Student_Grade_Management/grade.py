
from database import get_connection


class Grade:

    @staticmethod
    def add_marks():

        print("\n--- Enter Student Marks ---")

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

        subject = input("Enter Subject Name: ").strip()

        if not subject:
            print("Subject name cannot be empty!")
            connection.close()
            return

        try:
            marks = float(input("Enter Obtained Marks: "))
            max_marks = float(input("Enter Maximum Marks: "))

            if max_marks <= 0:
                print("Maximum marks must be greater than zero!")
                connection.close()
                return

            if marks < 0 or marks > max_marks:
                print("Invalid marks! Check the maximum marks.")
                connection.close()
                return

        except ValueError:
            print("Marks must be numeric!")
            connection.close()
            return

        cursor.execute("""
            INSERT INTO marks
                (student_id, subject, marks, max_marks)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(student_id, subject)
            DO UPDATE SET
                marks = excluded.marks,
                max_marks = excluded.max_marks
        """, (student_id, subject, marks, max_marks))

        connection.commit()
        connection.close()

        print("\nMarks saved successfully!")
        print("Student:", student[0])
        print("Subject:", subject)
        print("Marks:", marks, "/", max_marks)

    @staticmethod
    def calculate_grade(percentage):

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        elif percentage >= 35:
            return "E"
        else:
            return "F"

    @staticmethod
    def get_result(student_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT subject, marks, max_marks
            FROM marks
            WHERE student_id = ?
            ORDER BY subject
        """, (student_id,))

        records = cursor.fetchall()
        connection.close()

        if not records:
            return None

        total_marks = sum(row[1] for row in records)
        maximum_marks = sum(row[2] for row in records)

        percentage = (total_marks / maximum_marks) * 100

        failed_subjects = [
            row[0] for row in records
            if (row[1] / row[2]) * 100 < 35
        ]

        result = "PASS" if not failed_subjects else "FAIL"

        grade = (
            Grade.calculate_grade(percentage)
            if result == "PASS"
            else "F"
        )

        return {
            "subjects": records,
            "total": total_marks,
            "maximum": maximum_marks,
            "percentage": percentage,
            "grade": grade,
            "result": result,
            "failed_subjects": failed_subjects
        }