import os
import json
from typing import List
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

class JsonHandler(BaseHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath
        # make sure file exists; if not, create empty JSON array
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def persist(self, entry: LogEntry) -> None:
        # load existing logs or start fresh
        try:
            logs = self.retrieve_all()
        except Exception:
            logs = []
        logs.append(entry)

        # overwrite the file with updated log list
        with open(self.filepath, 'w') as f:
            json.dump([log.to_dict() for log in logs], f, indent=4)

    def retrieve_all(self) -> List[LogEntry]:
        # nothing to read from = return empty
        if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
            return []

        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [LogEntry.from_dict(item) for item in data]
        except Exception:
            return []
