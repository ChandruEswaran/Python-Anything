
from database import create_tables
from student import Student
from grade import Grade
from report import Report


def display_menu():

    print("\n")
    print("=" * 50)
    print("       STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Enter Student Marks")
    print("5. Generate Student Report")
    print("6. Delete Student")
    print("7. Exit")

    print("=" * 50)


def main():

    # Create database and tables
    create_tables()

    while True:

        display_menu()

        choice = input("Enter Your Choice (1-7): ").strip()

        if choice == "1":

            Student.add_student()

        elif choice == "2":

            Student.view_students()

        elif choice == "3":

            Student.search_student()

        elif choice == "4":

            Grade.add_marks()

        elif choice == "5":

            Report.generate_report()

        elif choice == "6":

            Student.delete_student()

        elif choice == "7":

            print("\nThank you for using Student Grade Management System!")
            break

        else:

            print("\nInvalid choice! Please select 1 to 7.")


if __name__ == "__main__":
    main()