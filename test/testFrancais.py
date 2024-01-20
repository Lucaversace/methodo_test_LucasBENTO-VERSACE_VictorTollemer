import unittest
from francais import Francais
from momentDeLaJournee import TempsJournee

class TestFrancais(unittest.TestCase):

    def setUp(self):
        self.langue = Francais()

    def test_saluer(self):
        self.assertEqual(self.langue.saluer(TempsJournee.SOIREE), "Bonsoir")

    def test_feliciter(self):
        self.assertEqual(self.langue.feliciter(), "Bien dit !")

if __name__ == '__main__':
    unittest.main()
