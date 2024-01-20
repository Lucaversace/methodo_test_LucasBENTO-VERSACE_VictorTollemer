from langues import InterfaceLangue
from momentDeLaJournee import TempsJournee

class VerificateurPalindrome:
    def __init__(self, langue: InterfaceLangue, moment_journee: TempsJournee):
        self.langue = langue
        self.moment_journee = moment_journee

    def verifier(self, chaine: str):
        return "Réponse"