import os
from typing import List
from datetime import datetime
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

class FileHandler(BaseHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath
        # make sure file exists
        if not os.path.exists(self.filepath):
            open(self.filepath, 'w').close()

    def persist(self, entry: LogEntry) -> None:
        # append single-line log (timestamp + level + message)
        line = f"{entry.date.isoformat()} {entry.level} {entry.message}\n"
        with open(self.filepath, 'a') as f:
            f.write(line)

    def retrieve_all(self) -> List[LogEntry]:
        if not os.path.exists(self.filepath):
            return []

        entries = []
        with open(self.filepath, 'r') as f:
            for line in f:
                parts = line.strip().split(' ', 2)
                if len(parts) == 3:
                    try:
                        entries.append(LogEntry(
                            date=datetime.fromisoformat(parts[0]),
                            level=parts[1],
                            message=parts[2]
                        ))
                    except:
                        continue  # skip corrupted line
        return entries
