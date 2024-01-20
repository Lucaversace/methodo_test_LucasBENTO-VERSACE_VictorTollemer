from langueinterface import LangueInterface
from expressions import Expressions

class LangueFrancaise(LangueInterface):
    def saluer(self, moment):
        if moment == 'BONJOUR':
            return Expressions.BONJOUR['fr']
        else:
            return Expressions.BONSOIR['fr']

    def feliciter(self):
        return Expressions.BIEN_DIT['fr']

    def acquitter(self, moment):
        return Expressions.AU_REVOIR['fr']
