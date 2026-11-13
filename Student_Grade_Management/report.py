
from database import get_connection
from grade import Grade


class Report:

    @staticmethod
    def generate_report():

        print("\n--- Student Result Report ---")

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

        if not student:
            print("Student not found!")
            return

        result = Grade.get_result(student_id)

        if result is None:
            print("Marks not entered for this student!")
            return

        print("\n" + "=" * 55)
        print("             STUDENT RESULT REPORT")
        print("=" * 55)

        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Age        :", student[2])
        print("Class      :", student[3])

        print("-" * 55)
        print(f"{'Subject':<22}{'Marks':>12}{'Maximum':>15}")
        print("-" * 55)

        for subject, marks, maximum in result["subjects"]:

            print(
                f"{subject:<22}"
                f"{marks:>12.2f}"
                f"{maximum:>15.2f}"
            )

        print("-" * 55)

        print(
            f"Total Marks : "
            f"{result['total']:.2f} / {result['maximum']:.2f}"
        )

        print(
            f"Percentage  : "
            f"{result['percentage']:.2f}%"
        )

        print("Grade       :", result["grade"])
        print("Result      :", result["result"])

        if result["failed_subjects"]:
            print(
                "Failed Subjects:",
                ", ".join(result["failed_subjects"])
            )

        print("=" * 55)