from abc import ABC, abstractmethod


class HistoryView(ABC):

    @abstractmethod
    def open(self): pass
