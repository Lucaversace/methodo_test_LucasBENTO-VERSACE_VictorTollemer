from enum import Enum

class TempsJournee(Enum):
    INCONNU = "Inconnu"
    MATIN = "Matin"
    APRES_MIDI = "Après-Midi"
    SOIREE = "Soirée"
    NUIT = "Nuit"

    def __str__(self):
        return self.value
