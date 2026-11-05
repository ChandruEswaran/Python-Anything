
from database import get_connection
from datetime import datetime, date
import calendar


class Report:

    @staticmethod
    def daily_report():

        print("\n--- Daily Attendance Summary ---")

        attendance_date = input(
            "Enter Date (YYYY-MM-DD), press Enter for today: "
        ).strip()

        if not attendance_date:

            attendance_date = date.today().isoformat()

        try:

            parsed_date = datetime.strptime(
                attendance_date, "%Y-%m-%d"
            ).date()

            if parsed_date > date.today():

                print("Future dates are not allowed!")
                return

        except ValueError:

            print("Invalid date format!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                COUNT(*),
                SUM(CASE WHEN status = 'P' THEN 1 ELSE 0 END),
                SUM(CASE WHEN status = 'A' THEN 1 ELSE 0 END),
                SUM(CASE WHEN status = 'L' THEN 1 ELSE 0 END)

            FROM attendance

            WHERE attendance_date = ?

        """, (attendance_date,))

        total, present, absent, leave = cursor.fetchone()

        connection.close()

        total = total or 0
        present = present or 0
        absent = absent or 0
        leave = leave or 0

        not_marked = None

        print("\n" + "=" * 45)
        print("       DAILY ATTENDANCE SUMMARY")
        print("=" * 45)

        print("Date          :", attendance_date)
        print("Total Marked  :", total)
        print("Present       :", present)
        print("Absent        :", absent)
        print("Leave         :", leave)

        print("=" * 45)

    @staticmethod
    def monthly_report():

        print("\n--- Monthly Attendance Report ---")

        try:

            year = int(input("Enter Year (YYYY): "))
            month = int(input("Enter Month (1-12): "))

            if month < 1 or month > 12:

                print("Invalid month!")
                return

            if year < 1900 or year > date.today().year:

                print("Invalid year!")
                return

            if (
                year == date.today().year
                and month > date.today().month
            ):

                print("Future months are not allowed!")
                return

        except ValueError:

            print("Enter valid year and month!")
            return

        start_date = f"{year}-{month:02d}-01"

        last_day = calendar.monthrange(
            year, month
        )[1]

        end_date = f"{year}-{month:02d}-{last_day:02d}"

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                m.member_id,
                m.name,

                COUNT(a.attendance_id),

                SUM(
                    CASE WHEN a.status = 'P'
                    THEN 1 ELSE 0 END
                ),

                SUM(
                    CASE WHEN a.status = 'A'
                    THEN 1 ELSE 0 END
                ),

                SUM(
                    CASE WHEN a.status = 'L'
                    THEN 1 ELSE 0 END
                )

            FROM members m

            LEFT JOIN attendance a
                ON m.member_id = a.member_id

                AND a.attendance_date
                BETWEEN ? AND ?

            GROUP BY m.member_id, m.name

            ORDER BY m.member_id

        """, (start_date, end_date))

        records = cursor.fetchall()

        connection.close()

        if not records:

            print("No registered members found!")
            return

        print("\n" + "=" * 100)
        print("                 MONTHLY ATTENDANCE REPORT")
        print("=" * 100)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Total':<10}"
            f"{'Present':<12}"
            f"{'Absent':<12}"
            f"{'Leave':<10}"
            f"{'Percentage':<12}"
        )

        print("-" * 100)

        for record in records:

            member_id = record[0]
            name = record[1]

            total = record[2] or 0
            present = record[3] or 0
            absent = record[4] or 0
            leave = record[5] or 0

            percentage = (
                (present / total) * 100
                if total > 0
                else 0
            )

            print(
                f"{member_id:<8}"
                f"{name:<20}"
                f"{total:<10}"
                f"{present:<12}"
                f"{absent:<12}"
                f"{leave:<10}"
                f"{percentage:.2f}%"
            )

        print("=" * 100)

    @staticmethod
    def individual_history():

        print("\n--- Individual Attendance History ---")

        try:

            member_id = int(
                input("Enter Member ID: ")
            )

        except ValueError:

            print("Invalid Member ID!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name
            FROM members
            WHERE member_id = ?
        """, (member_id,))

        member = cursor.fetchone()

        if not member:

            print("Member not found!")
            connection.close()
            return

        cursor.execute("""
            SELECT
                attendance_date,
                status,
                remarks

            FROM attendance

            WHERE member_id = ?

            ORDER BY attendance_date DESC

        """, (member_id,))

        records = cursor.fetchall()

        connection.close()

        print("\nMember Name:", member[0])

        if not records:

            print("No attendance records found!")
            return

        print("-" * 65)

        print(
            f"{'Date':<18}"
            f"{'Status':<18}"
            f"{'Remarks':<25}"
        )

        print("-" * 65)

        present = 0
        absent = 0
        leave = 0

        status_names = {
            "P": "Present",
            "A": "Absent",
            "L": "Leave"
        }

        for record in records:

            status = record[1]

            if status == "P":
                present += 1

            elif status == "A":
                absent += 1

            elif status == "L":
                leave += 1

            print(
                f"{record[0]:<18}"
                f"{status_names[status]:<18}"
                f"{(record[2] or '-'):<25}"
            )

        total = len(records)

        percentage = (present / total) * 100

        print("-" * 65)

        print("Total Marked Days:", total)
        print("Present Days     :", present)
        print("Absent Days      :", absent)
        print("Leave Days       :", leave)

        print(
            f"Attendance Percentage: {percentage:.2f}%"
        )

        print("-" * 65)
