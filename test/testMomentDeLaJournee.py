import unittest
from momentDeLaJournee import TempsJournee

class TestTempsJournee(unittest.TestCase):

    def test_temps_journee_str(self):
        self.assertEqual(str(TempsJournee.MATIN), "Matin")
        self.assertEqual(str(TempsJournee.SOIREE), "Soirée")

if __name__ == '__main__':
    unittest.main()
