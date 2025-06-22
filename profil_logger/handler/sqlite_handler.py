import sqlite3
from typing import List
from datetime import datetime
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

class SQLLiteHandler(BaseHandler):
    def __init__(self, db_path: str, table_name: str = "logs"):
        self.db_path = db_path
        self.table_name = table_name
        self._create_table()

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        # create table if not exists
        with self._get_conn() as conn:
            conn.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    level TEXT NOT NULL,
                    message TEXT NOT NULL
                );
            """)

    def persist(self, entry: LogEntry) -> None:
        # insert new log safely using placeholders
        with self._get_conn() as conn:
            conn.execute(
                f"INSERT INTO {self.table_name} (timestamp, level, message) VALUES (?, ?, ?)",
                (entry.date.isoformat(), entry.level, entry.message)
            )

    def retrieve_all(self) -> List[LogEntry]:
        entries: List[LogEntry] = []
        try:
            with self._get_conn() as conn:
                rows = conn.execute(
                    f"SELECT timestamp, level, message FROM {self.table_name} ORDER BY timestamp"
                ).fetchall()

                for ts, lvl, msg in rows:
                    try:
                        entries.append(LogEntry(datetime.fromisoformat(ts), lvl, msg))
                    except:
                        continue  # skip broken row
        except:
            return []
        return entries
