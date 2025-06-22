import csv
import os
from typing import List
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

class CSVHandler(BaseHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath

        # create file and write header if it doesn’t exist or is empty
        if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
            with open(self.filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["date", "level", "msg"])

    def persist(self, entry: LogEntry) -> None:
        # just append a new row to the file
        with open(self.filepath, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                entry.date.isoformat(),
                entry.level,
                entry.message
            ])

    def retrieve_all(self) -> List[LogEntry]:
        if not os.path.exists(self.filepath):
            return []

        entries: List[LogEntry] = []
        try:
            with open(self.filepath, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entries.append(LogEntry.from_dict(row))
        except Exception:
            return []

        return entries
