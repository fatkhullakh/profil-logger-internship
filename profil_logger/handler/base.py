# base.py

from abc import ABC, abstractmethod
from profil_logger.models import LogEntry
from typing import List

class BaseHandler(ABC):

    @abstractmethod
    def persist(self, entry: LogEntry) -> None:
        ...

    @abstractmethod
    def retrieve_all(self) -> List[LogEntry]:
        ...
