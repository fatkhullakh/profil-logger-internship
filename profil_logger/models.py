from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class LogEntry:
    date: datetime
    level: str
    message: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "date": self.date.isoformat(),
            "level": self.level,
            "message": self.message
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> "LogEntry":
        return LogEntry(
            date=datetime.fromisoformat(data["date"]),
            level=data["level"],
            message=data["message"]
        )