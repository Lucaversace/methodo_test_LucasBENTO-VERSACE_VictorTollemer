from .expressions import Salutations
from .momentDeLaJournee import TempsJournee
from .langues import InterfaceLangue

class Anglais(InterfaceLangue):

    def dire_au_revoir(self):
        return Salutations.GOODBYE

    def saluer(self, moment: TempsJournee):
        return Salutations.HELLO

    def feliciter(self):
        return Salutations.WELL_SAID

    def __str__(self):
        return "Anglais"
