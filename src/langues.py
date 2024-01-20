from abc import ABC, abstractmethod
from momentDeLaJournee import TempsJournee

class InterfaceLangue(ABC):

    @abstractmethod
    def feliciter(self):
        pass

    @abstractmethod
    def saluer(self, moment: TempsJournee):
        pass

    @abstractmethod
    def dire_au_revoir(self):
        pass
