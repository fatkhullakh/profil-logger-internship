# ProfilLogger

Hey there 👋

This is a simple logging library I built as part of a backend internship task.  
It lets you log messages to different formats like JSON, CSV, plain text, or even a SQLite database.

The idea was to take a messy codebase and turn it into something clean, modular, and reliable — all in pure Python with no third-party packages.

---

## 🛠 What it does

- Logs messages at different levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Supports multiple output formats (via handlers)
- Lets you search and group logs using a Reader tool
- Clean object-oriented design
- Fully tested with `pytest`
- Built for Python 3.12+ (no external libraries)

---

## 💡 How to use it

First, create a logger and attach one or more handlers:

```python
from profil_logger.logger import ProfilLogger
from profil_logger.handlers.json_handler import JsonHandler

logger = ProfilLogger([JsonHandler("logs.json")])
logger.info("User signed in")
logger.error("Something went wrong")
