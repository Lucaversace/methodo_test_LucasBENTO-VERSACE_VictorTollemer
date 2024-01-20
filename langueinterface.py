from abc import ABC, abstractmethod

class LangueInterface(ABC):
    @abstractmethod
    def saluer(self, moment):
        pass

    @abstractmethod
    def feliciter(self):
        pass

    @abstractmethod
    def acquitter(self, moment):
        pass
