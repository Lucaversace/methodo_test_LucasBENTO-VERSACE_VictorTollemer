import unittest
from src.anglais import Anglais
from src.momentDeLaJournee import TempsJournee

class TestAnglais(unittest.TestCase):

    def setUp(self):
        self.langue = Anglais()

    def test_saluer(self):
        self.assertEqual(self.langue.saluer(TempsJournee.MATIN), "Hello")

    def test_feliciter(self):
        self.assertEqual(self.langue.feliciter(), "Well Said!")

if __name__ == '__main__':
    unittest.main()
