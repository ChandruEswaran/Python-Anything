from database import get_connection

class Member:

    @staticmethod
    def add_member():

        print("\n--- Register New Member ---")

        name = input("Enter Member Name: ").strip()

        if not name:
            print("Member name cannot be empty!")
            return

        try:

            age = int(input("Enter Age: "))

            if age <= 0 or age > 120:

                print("Enter a valid age!")
                return

        except ValueError:

            print("Age must be a number!")
            return

        department = input(
            "Enter Department / Class: "
        ).strip()

        if not department:

            print("Department cannot be empty!")
            return

        phone = input(
            "Enter Phone Number: "
        ).strip()

        if phone and (
            not phone.isdigit() or len(phone) != 10
        ):

            print("Enter a valid 10-digit phone number!")
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO members
                (name, age, department, phone)

            VALUES (?, ?, ?, ?)

        """, (name, age, department, phone))

        connection.commit()

        member_id = cursor.lastrowid

        connection.close()

        print("\nMember registered successfully!")
        print("Member ID:", member_id)

    @staticmethod
    def view_members():

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                member_id,
                name,
                age,
                department,
                phone

            FROM members

            ORDER BY member_id
        """)

        members = cursor.fetchall()

        connection.close()

        print("\n--- Registered Members ---")

        if not members:

            print("No members found!")
            return

        print("-" * 85)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Age':<8}"
            f"{'Department':<22}"
            f"{'Phone':<15}"
        )

        print("-" * 85)

        for member in members:

            print(
                f"{member[0]:<8}"
                f"{member[1]:<20}"
                f"{member[2]:<8}"
                f"{member[3]:<22}"
                f"{member[4] or '-':<15}"
            )

        print("-" * 85)

    @staticmethod
    def search_member():

        print("\n--- Search Member ---")

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
            SELECT *
            FROM members
            WHERE member_id = ?
        """, (member_id,))

        member = cursor.fetchone()

        connection.close()

        if member:

            print("\nMember Found!")

            print("Member ID :", member[0])
            print("Name      :", member[1])
            print("Age       :", member[2])
            print("Department:", member[3])
            print("Phone     :", member[4])
            print("Created At:", member[5])

        else:

            print("Member not found!")

    @staticmethod
    def update_member():

        print("\n--- Update Member Details ---")

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
            SELECT name, age, department, phone
            FROM members
            WHERE member_id = ?
        """, (member_id,))

        member = cursor.fetchone()

        if not member:

            print("Member not found!")
            connection.close()
            return

        print("\nCurrent Details:")

        print("Name      :", member[0])
        print("Age       :", member[1])
        print("Department:", member[2])
        print("Phone     :", member[3])

        print("\nEnter new details.")

        name = input(
            "Enter Name: "
        ).strip()

        if not name:
            print("Name cannot be empty!")
            connection.close()
            return

        try:

            age = int(input("Enter Age: "))

            if age <= 0 or age > 120:

                print("Invalid age!")
                connection.close()
                return

        except ValueError:

            print("Age must be numeric!")
            connection.close()
            return

        department = input(
            "Enter Department: "
        ).strip()

        if not department:

            print("Department cannot be empty!")
            connection.close()
            return

        phone = input(
            "Enter Phone Number: "
        ).strip()

        if phone and (
            not phone.isdigit() or len(phone) != 10
        ):

            print("Invalid phone number!")
            connection.close()
            return

        cursor.execute("""
            UPDATE members

            SET
                name = ?,
                age = ?,
                department = ?,
                phone = ?

            WHERE member_id = ?

        """, (
            name,
            age,
            department,
            phone,
            member_id
        ))

        connection.commit()
        connection.close()

        print("\nMember details updated successfully!")

    @staticmethod
    def delete_member():

        print("\n--- Delete Member ---")

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

        confirm = input(
            f"Delete member {member[0]}? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            cursor.execute("""
                DELETE FROM members
                WHERE member_id = ?
            """, (member_id,))

            connection.commit()

            print(
                "Member and associated attendance records "
                "deleted successfully!"
            )

        else:

            print("Delete operation cancelled!")

        connection.close()
