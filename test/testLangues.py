import unittest
from francais import Francais
from anglais import Anglais
from langues import InterfaceLangue

class TestLangues(unittest.TestCase):

    def test_interface_implementation(self):
        self.assertTrue(issubclass(Francais, InterfaceLangue))
        self.assertTrue(issubclass(Anglais, InterfaceLangue))

    def test_str_method(self):
        francais = Francais()
        anglais = Anglais()
        self.assertEqual(str(francais), "Français")
        self.assertEqual(str(anglais), "Anglais")

if __name__ == '__main__':
    unittest.main()
