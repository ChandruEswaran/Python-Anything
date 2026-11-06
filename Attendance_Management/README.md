# Attendance Management System

The General Attendance Management System is a Python console application used to register members and maintain their daily attendance records.
The application allows an administrator to mark members as Present, Absent or Leave and generate daily, monthly and individual attendance reports.

## What it can do

1. Register new members.
2. View all registered members.
3. Search members by ID.
4. Update member details.
5. Mark daily attendance.
6. Change existing attendance records.
7. View daily attendance reports.
8. View monthly attendance reports.
9. Calculate attendance percentage.
10. View individual attendance history.
11. Delete member records.
12. Exit application.

## Technologies used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| SQLite 3 | Store member and attendance data |
| OOP | Organize application logic |
| Functions | Separate operations |
| Datetime | Manage attendance dates |
| Exception Handling | Handle invalid inputs |
| SQL | Database operations |


## Attendance rules

| Status | Meaning | Attendance value |
|---|---|---|
| P | Present | 1 |
| A | Absent | 0 |
| L | Leave | 0 |

```
Attendance % = Present Days / Total Marked Days * 100
```

## Sample application execution

### Main menu

```
=======================================================
         GENERAL ATTENDANCE MANAGEMENT SYSTEM
=======================================================
1. Register New Member
2. View All Members
3. Search Member
4. Update Member Details
5. Mark Daily Attendance
6. View Daily Attendance
7. Daily Attendance Summary
8. Monthly Attendance Report
9. Individual Attendance History
10. Delete Member
11. Exit
=======================================================
Enter Your Choice (1-11):
```

### Register a member

```
Enter Your Choice (1-11): 1

--- Register New Member ---

Enter Member Name: Arun Kumar
Enter Age: 25
Enter Department / Class: Python Development
Enter Phone Number: 9876543210

Member registered successfully!
Member ID: 1
```
```
Member ID: 2
Name: Kumar
Department: Python Development

Member ID: 3
Name: Priya
Department: Testing
```

### View registered members

```
Enter Your Choice (1-11): 2

--- Registered Members ---

-------------------------------------------------------------------------------------
ID      Name                Age     Department            Phone
-------------------------------------------------------------------------------------
1       Arun Kumar          25      Python Development    9876543210
2       Kumar               24      Python Development    9876543211
3       Priya               23      Testing               9876543212
-------------------------------------------------------------------------------------
```

### Mark daily attendance

```
Enter Your Choice (1-11): 5

--- Mark Daily Attendance ---

Enter Member ID: 1

Enter Date (YYYY-MM-DD), press Enter for today:

Member Name: Arun Kumar

Attendance Status:
P - Present
A - Absent
L - Leave

Enter Attendance Status: P
Enter Remarks (optional): On time

Attendance saved successfully!

Member Name: Arun Kumar
Date: 2026-11-03
Status: Present0
```

### View daily attendance

```
Enter Your Choice (1-11): 6

Enter Date (YYYY-MM-DD), press Enter for today:

Daily Attendance Report
Date: 2026-11-03

------------------------------------------------------------------------------------------
ID      Name                Department            Status         Remarks
------------------------------------------------------------------------------------------
1       Arun Kumar          Python Development    Present        On time
2       Kumar               Python Development    Absent         Not available
3       Priya               Testing               Leave          Personal leave
------------------------------------------------------------------------------------------
```

### Daily attendance summary

```
Enter Your Choice (1-11): 7

--- Daily Attendance Summary ---

Enter Date (YYYY-MM-DD), press Enter for today:

=============================================
       DAILY ATTENDANCE SUMMARY
=============================================
Date          : 2026-11-03
Total Marked  : 3
Present       : 1
Absent        : 1
Leave         : 1
=============================================
```

### Monthly attendance report

```
Enter Your Choice (1-11): 8

--- Monthly Attendance Report ---

Enter Year (YYYY): 2026
Enter Month (1-12): 11

====================================================================================================
                 MONTHLY ATTENDANCE REPORT
====================================================================================================
ID      Name                Total     Present     Absent      Leave     Percentage
----------------------------------------------------------------------------------------------------
1       Arun Kumar          20        18          1           1         90.00%
2       Kumar               20        15          3           2         75.00%
3       Priya               20        17          1           2         85.00%
====================================================================================================
```

### Individual attendance history

```
Enter Your Choice (1-11): 9

--- Individual Attendance History ---

Enter Member ID: 1

Member Name: Arun Kumar

-----------------------------------------------------------------
Date              Status            Remarks
-----------------------------------------------------------------
2026-11-03        Present           On time
2026-11-02        Present           -
2026-11-01        Absent            Not available
-----------------------------------------------------------------

Total Marked Days: 3
Present Days     : 2
Absent Days      : 1
Leave Days       : 0

Attendance Percentage: 66.67%
-----------------------------------------------------------------
```

## Run it

From this folder, run:

```bash
python main.py
```

Python 3 is required. No extra packages are needed. The app creates its SQLite database and tables when it starts.
