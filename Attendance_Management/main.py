
from database import create_tables

from member import Member

from attendance import Attendance

from report import Report


def display_menu():

    print("\n")

    print("=" * 55)
    print("          GENERAL ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Register New Member")
    print("2. View All Members")
    print("3. Search Member")
    print("4. Update Member Details")
    print("5. Mark Daily Attendance")
    print("6. View Daily Attendance")
    print("7. Daily Attendance Summary")
    print("8. Monthly Attendance Report")
    print("9. Individual Attendance History")
    print("10. Delete Member")
    print("11. Exit")

    print("=" * 55)


def main():

    # Initialize database
    create_tables()

    while True:

        display_menu()

        choice = input(
            "Enter Your Choice (1-11): "
        ).strip()

        if choice == "1":

            Member.add_member()

        elif choice == "2":

            Member.view_members()

        elif choice == "3":

            Member.search_member()

        elif choice == "4":

            Member.update_member()

        elif choice == "5":

            Attendance.mark_attendance()

        elif choice == "6":

            Attendance.view_attendance()

        elif choice == "7":

            Report.daily_report()

        elif choice == "8":

            Report.monthly_report()

        elif choice == "9":

            Report.individual_history()

        elif choice == "10":

            Member.delete_member()

        elif choice == "11":

            print(
                "\nThank you for using "
                "General Attendance Management System!"
            )

            break

        else:

            print(
                "\nInvalid choice! Please select 1 to 11."
            )


if __name__ == "__main__":

    main()
