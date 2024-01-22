import unittest
from src.verifPalindrome import VerificateurPalindrome
from src.francais import Francais
from src.momentDeLaJournee import TempsJournee

class TestVerificateurPalindrome(unittest.TestCase):

    def setUp(self):
        self.langue = Francais()
        self.verif_palindrome = VerificateurPalindrome(self.langue, TempsJournee.MATIN)

    def test_verifier_non_palindrome(self):
        self.assertNotEqual(self.verif_palindrome.verifier("python"), "Bien dit !")

    def test_verifier_palindrome(self):
        self.assertEqual(self.verif_palindrome.verifier("kayak"), "Bien dit !")

if __name__ == '__main__':
    unittest.main()
