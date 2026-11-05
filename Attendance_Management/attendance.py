
from database import get_connection
from datetime import datetime, date


class Attendance:

    @staticmethod
    def mark_attendance():

        print("\n--- Mark Daily Attendance ---")

        try:

            member_id = int(
                input("Enter Member ID: ")
            )

        except ValueError:

            print("Invalid Member ID!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        # Check whether member exists
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

        # Get attendance date
        attendance_date = input(
            "Enter Date (YYYY-MM-DD), press Enter for today: "
        ).strip()

        if not attendance_date:

            attendance_date = date.today().isoformat()

        # Validate date
        try:

            parsed_date = datetime.strptime(
                attendance_date, "%Y-%m-%d"
            ).date()

            if parsed_date > date.today():

                print("Future attendance dates are not allowed!")
                connection.close()
                return

        except ValueError:

            print("Invalid date! Use YYYY-MM-DD format.")
            connection.close()
            return

        print("\nMember Name:", member[0])

        print("\nAttendance Status:")
        print("P - Present")
        print("A - Absent")
        print("L - Leave")

        status = input(
            "Enter Attendance Status: "
        ).strip().upper()

        if status not in ["P", "A", "L"]:

            print("Invalid attendance status!")
            connection.close()
            return

        remarks = input(
            "Enter Remarks (optional): "
        ).strip()

        # Insert new attendance or update existing record
        cursor.execute("""
            INSERT INTO attendance (
                member_id,
                attendance_date,
                status,
                remarks
            )

            VALUES (?, ?, ?, ?)

            ON CONFLICT(member_id, attendance_date)

            DO UPDATE SET
                status = excluded.status,
                remarks = excluded.remarks

        """, (
            member_id,
            attendance_date,
            status,
            remarks
        ))

        connection.commit()
        connection.close()

        status_names = {
            "P": "Present",
            "A": "Absent",
            "L": "Leave"
        }

        print("\nAttendance saved successfully!")

        print("Member Name:", member[0])
        print("Date:", attendance_date)
        print("Status:", status_names[status])

    @staticmethod
    def view_attendance():

        print("\n--- View Daily Attendance ---")

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
                m.member_id,
                m.name,
                m.department,
                a.status,
                a.remarks

            FROM members m

            LEFT JOIN attendance a
                ON m.member_id = a.member_id
                AND a.attendance_date = ?

            ORDER BY m.member_id

        """, (attendance_date,))

        records = cursor.fetchall()

        connection.close()

        print("\nDaily Attendance Report")
        print("Date:", attendance_date)

        if not records:

            print("No registered members found!")
            return

        print("-" * 90)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Department':<22}"
            f"{'Status':<15}"
            f"{'Remarks':<20}"
        )

        print("-" * 90)

        for record in records:

            status_names = {
                "P": "Present",
                "A": "Absent",
                "L": "Leave"
            }

            status = (
                status_names.get(record[3], "Not Marked")
                if record[3]
                else "Not Marked"
            )

            print(
                f"{record[0]:<8}"
                f"{record[1]:<20}"
                f"{record[2]:<22}"
                f"{status:<15}"
                f"{(record[4] or '-'):<20}"
            )

        print("-" * 90)
