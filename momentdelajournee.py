from datetime import datetime

class MomentDeLaJournee:
    @staticmethod
    def obtenir_moment():
        heure_actuelle = datetime.now().hour
        if 5 <= heure_actuelle < 18:
            return 'BONJOUR'
        else:
            return 'BONSOIR'
