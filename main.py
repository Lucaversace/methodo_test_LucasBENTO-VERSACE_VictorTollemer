from francais import Francais
from anglais import Anglais
from ohce import Echo
from momentDeLaJournee import TempsJournee

class SystemLangAdapter:
    def __init__(self):
        self.langue = Anglais()

if __name__ == '__main__':
    ohce = Echo(SystemLangAdapter().langue, TempsJournee.MATIN)

