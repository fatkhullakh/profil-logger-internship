# profil-logger-internship
Author: Fatkhullakh Turakhonov

Hi there 👋  
This is my submission for the **Profil Software backend internship task**.  
The project is a fully refactored, testable logging library written in **Python 3.12+**, with clean code, OOP design, and support for multiple storage backends.

---

## 🚀 What This Library Does

The logging system lets you:

- Log messages at different levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- Save logs to:
  - `.json` file
  - `.csv` file
  - Plain text `.log` file
  - SQLite database
- Read logs with filtering:
  - By text
  - By regex
  - By date range
- Group logs:
  - By level
  - By month

---

## 📁 Project Structure
profil_logger/
├── handler/ # Handlers for saving logs to various formats
│ ├── base.py
│ ├── json_handler.py
│ ├── csv_handler.py
│ ├── file_handler.py
│ └── sqlite_handler.py
├── tests/ # Unit tests using pytest
│ ├── test_logger.py
│ └── test_reader.py
├── logger.py # Main logging interface
├── reader.py # Log reading & filtering logic
├── models.py # LogEntry dataclass
├── init.py
├── pyproject.toml # Config file for ruff (linter)
└── README.md # This file
