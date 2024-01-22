import locale
from src.anglais import Anglais
from src.francais import Francais
from src.ohce import Echo
from src.momentDeLaJournee import TempsJournee


class LangueSystem:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')
        langue_systeme = locale.getlocale()[0]

        if langue_systeme and langue_systeme.startswith('en_'):
            self.langue = Anglais()
        else:
            self.langue = Francais()

if __name__ == '__main__':
    ohce = Echo(LangueSystem().langue, TempsJournee.MATIN)
