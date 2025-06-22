from datetime import datetime
from typing import List
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

# basic levels to control verbosity
LOG_LEVEL_VALUES = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
DEFAULT_LOG_LEVEL = "DEBUG"

class ProfilLogger:
    def __init__(self, handlers: List[BaseHandler]):
        # takes a list of handlers (JSON, SQLite, etc)
        self.handlers = handlers
        self.current_log_level_val = LOG_LEVEL_VALUES[DEFAULT_LOG_LEVEL]

    def _log(self, level: str, msg: str):
        # skip if the log level is too low
        if LOG_LEVEL_VALUES[level] < self.current_log_level_val:
            return

        # create log entry and pass it to each handler
        entry = LogEntry(date=datetime.now(), level=level, message=msg)
        for handler in self.handlers:
            try:
                handler.persist(entry)
            except Exception as e:
                # don't kill the whole app if one handler fails
                print(f"[ERROR] Handler {type(handler).__name__} failed: {e}")

    # quick shortcuts to log with different levels
    def info(self, msg: str): self._log("INFO", msg)
    def warning(self, msg: str): self._log("WARNING", msg)
    def error(self, msg: str): self._log("ERROR", msg)
    def critical(self, msg: str): self._log("CRITICAL", msg)
    def debug(self, msg: str): self._log("DEBUG", msg)

    def set_log_level(self, level: str):
        # let user change log level at runtime
        if level.upper() in LOG_LEVEL_VALUES:
            self.current_log_level_val = LOG_LEVEL_VALUES[level.upper()]
