# Student Grade Management

Student Grade Management System is a Python-based application used to manage student details, enter subject-wise marks, calculate total marks, average, grades and pass/fail status. A simple way to keep student records and marks organized. This menu-driven app stores student information locally and turns subject scores into individual reports.

Instead of calculating marks manually, this application automatically calculates and stores student results in an SQLite database.

## Main functionalities

1. Add new student.
2. View all students.
3. Search student by ID.
4. Enter subject-wise marks.
5. Calculate total marks.
6. Calculate average percentage.
7. Calculate grade.
8. Display pass/fail result.
9. Generate individual student report.
10. Delete student records.

### Grade calculation rules

| Percentage | Grade |
|---|---|
| 90–100 | `A+` |
| 80–89.99 | `A` |
| 70–79.99 | `B` |
| 60–69.99 | `C` |
| 50–59.99 | `D` |
| 35–49.99 | `E` |
| Below 35 | `F` |

### Important logic explanation

1. `add_marks()` gets the student ID and checks whether the student exists.
2. It collects the subject and marks.
3. It validates obtained marks against maximum marks.
4. It inserts the marks into `SQLite`.
5. If the same subject already exists for that student, it updates the existing marks.
6. `calculate_grade()` determines the grade based on percentage.
7. `get_result()` retrieves all subject marks and calculates the overall result.

For example
- Mathematics: 90/100
- Physics: 80/100
- Chemistry: 75/100
- Computer Science: 85/100
- English: 70/100

```
Total = 400/500
Percentage = 80%

Grade = A  --> Result = PASS
```
> **Note:** If even one subject is below 35%, the overall result becomes FAIL, and the displayed grade becomes F.

## STUDENT GRADE MANAGEMENT SYSTEM

```
==================================================
       STUDENT GRADE MANAGEMENT SYSTEM
==================================================
1. Add New Student
2. View All Students
3. Search Student
4. Enter Student Marks
5. Generate Student Report
6. Delete Student
7. Exit
==================================================
Enter Your Choice (1-7):
```
Example 1: Add student

```
Enter Your Choice (1-7): 1

--- Add New Student ---

Enter Student Name: Arun Kumar
Enter Student Age: 18
Enter Class Name: 12th Standard

Student added successfully!
Student ID: 1
```
Example 2: Enter subject marks

```
Enter Your Choice (1-7): 4

--- Enter Student Marks ---

Enter Student ID: 1
Enter Subject Name: Mathematics
Enter Obtained Marks: 90
Enter Maximum Marks: 100

Marks saved successfully!
Student: Arun Kumar
Subject: Mathematics
Marks: 90.0 / 100.0
```
Example 3: Generate result report

```
Enter Your Choice (1-7): 5

Enter Student ID: 1

=======================================================
             STUDENT RESULT REPORT
=======================================================
Student ID : 1
Name       : Arun Kumar
Age        : 18
Class      : 12th Standard
-------------------------------------------------------
Subject                       Marks       Maximum
-------------------------------------------------------
Chemistry                     75.00         100.00
Computer Science               85.00         100.00
English                        70.00         100.00
Mathematics                    90.00         100.00
Physics                        80.00         100.00
-------------------------------------------------------
Total Marks : 400.00 / 500.00
Percentage  : 80.00%
Grade       : A
Result      : PASS
=======================================================
```

## What it can do

- Add, search, list, and remove students
- Enter marks for each subject
- Generate student reports
- Store records in a local SQLite database

## Run it

From this folder, run:

```bash
python main.py
```

Python 3 is required; no third-party packages are needed. The app creates its database tables when it starts.
