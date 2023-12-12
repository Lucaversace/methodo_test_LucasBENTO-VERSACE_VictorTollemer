from langueinterface import LangueInterface
from expressions import Expressions

class LangueAnglaise(LangueInterface):
    def saluer(self, moment):
        if moment == 'BONJOUR':
            return Expressions.BONJOUR['en']
        else:
            return Expressions.BONSOIR['en']

    def feliciter(self):
        return Expressions.BIEN_DIT['en']

    def acquitter(self, moment):
        return Expressions.AU_REVOIR['en']
