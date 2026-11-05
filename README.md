# Python_Anything

**A collection of small ideas, useful tools, and learning projects — each one a step toward building something real.**

Welcome! This repository brings together Python projects built to explore everyday problems, from sorting a list and drawing a heart to managing bookings, bills, attendance, and student records. Pick a folder, run a project, and make it your own.

## Projects

| Project | What you'll find |
|---|---|
| [Attendance Management](./Attendance_Management/README.md) | Member records, attendance tracking, and reports with SQLite |
| [Banking System](./Banking%20System/README.md) | A small command-line deposit, withdrawal, and balance demo |
| [Bubble Sort Project](./Bubble_Sort_Project/README.md) | Interactive ascending and descending bubble sort |
| [Bus Ticket Booking](./Bus_ticket_booking/README.md) | A Flask booking app backed by SQLite |
| [Dairy Shop Billing System](./Dairy_Shop_Billing_System/README.md) | Customers, products, invoices, stock, and sales reports |
| [Heart Drawing](./HeartDrawing/README.md) | A heart-inspired shape drawn with Turtle graphics |
| [OTP Verification System](./OTP_Verification_System/README.md) | Email-based one-time password verification |
| [Pizza Bill Calculator](./Pizza%20Order/README.md) | A simple interactive pizza order and bill calculator |
| [Simple Task Maker](./Simple%20Task%20maker/README.md) | An in-memory command-line task manager |
| [Gmail and Zoho SMTP Tests](./Smtp_test/README.md) | Shared, configurable SMTP test scripts |
| [Student Grade Management](./Student_Grade_Management/README.md) | Student records, marks, and reports with SQLite |

Each project folder has its own README with its run instructions and requirements. Most projects use only Python's standard library; the Bus Ticket Booking app and OTP Verification System have additional setup described in their project guides.

## Getting started

1. Install Python 3.
2. Open the project folder you'd like to try.
3. Follow that folder's README to install any project-specific dependencies.
4. Run its entry-point script from that folder.

For example:

```bash
cd Bubble_Sort_Project
python main.py
```

## Standalone utilities

Three scripts live at the repository root:

- `test.py` and `test_api.py` make authenticated SAP API requests and print response details.
- `sql_executor.py` runs a configured list of SQL files against SQL Server and writes a timestamped log.

These are environment-specific integration tools, not local demos. They require access to the relevant SAP service or SQL Server, and `sql_executor.py` also needs the referenced SQL files in a configured folder. Set credentials and settings in environment variables before running:

| Variable | Used by |
|---|---|
| `SAP_API_URL` | `test.py`, `test_api.py` (full endpoint URL) |
| `SAP_API_USERNAME`, `SAP_API_PASSWORD` | `test.py`, `test_api.py` |
| `SQL_SERVER`, `SQL_DATABASE`, `SQL_USERNAME`, `SQL_PASSWORD` | `sql_executor.py` |
| `SQL_FOLDER` | `sql_executor.py` (folder containing the SQL files) |

The API scripts require `requests`; the SQL utility requires `pyodbc` and a compatible Microsoft SQL Server ODBC driver. Install the Python packages with `python -m pip install requests pyodbc` if you need these utilities.

For PowerShell, set variables for the current terminal session like this:

```powershell
$env:SAP_API_URL = "your-full-endpoint"
$env:SAP_API_USERNAME = "your-user"
$env:SAP_API_PASSWORD = "your-password"
```

Only configure the variables for the utility you intend to use. Never put real credentials in source code or commit them to GitHub. Credentials that were previously present in these scripts should be rotated before reuse. The repository's `.gitignore` excludes `.env` files and local database files; check `git status` before publishing.

## A note on learning

These projects are small on purpose: each is a place to experiment, improve, and learn by doing. Contributions, thoughtful suggestions, and beginner-friendly improvements are welcome.
