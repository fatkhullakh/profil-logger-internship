import re
from typing import List, Optional, Dict
from datetime import datetime
from profil_logger.models import LogEntry
from profil_logger.handler.base import BaseHandler

class ProfilLoggerReader:
    def __init__(self, handler: BaseHandler):
        # expects one handler to read logs from (JSON, CSV, etc)
        self.handler = handler

    def _filter_by_date(
        self,
        logs: List[LogEntry],
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[LogEntry]:
        # filters logs to match date range if provided
        return [
            log for log in logs
            if (not start_date or log.date >= start_date)
            and (not end_date or log.date < end_date)
        ]

    def find_by_text(self, text: str, start_date=None, end_date=None) -> List[LogEntry]:
        # grab logs that contain the given string
        logs = self.handler.retrieve_all()
        return self._filter_by_date(
            [log for log in logs if text in log.message],
            start_date, end_date
        )

    def find_by_regex(self, pattern: str, start_date=None, end_date=None) -> List[LogEntry]:
        try:
            regex = re.compile(pattern)
        except re.error:
            return []  # bad regex = no results

        logs = self.handler.retrieve_all()
        return self._filter_by_date(
            [log for log in logs if regex.search(log.message)],
            start_date, end_date
        )

    def groupby_level(self, start_date=None, end_date=None) -> Dict[str, List[LogEntry]]:
        # sort logs into buckets by log level
        logs = self._filter_by_date(self.handler.retrieve_all(), start_date, end_date)
        result = {}
        for log in logs:
            result.setdefault(log.level, []).append(log)
        return result

    def groupby_month(self, start_date=None, end_date=None) -> Dict[str, List[LogEntry]]:
        # sort logs into buckets like '2025-06', '2025-07', etc.
        logs = self._filter_by_date(self.handler.retrieve_all(), start_date, end_date)
        result = {}
        for log in logs:
            key = log.date.strftime('%Y-%m')
            result.setdefault(key, []).append(log)
        return result
