from expressions import Salutations
from momentDeLaJournee import TempsJournee
from langues import InterfaceLangue

class Francais(InterfaceLangue):

    def dire_au_revoir(self):
        return Salutations.AU_REVOIR

    def saluer(self, moment: TempsJournee):
        if moment in [TempsJournee.SOIREE, TempsJournee.NUIT]:
            return Salutations.BONSOIR
        return Salutations.BONJOUR

    def feliciter(self):
        return Salutations.BIEN_DIT

    def __str__(self):
        return "Français"
