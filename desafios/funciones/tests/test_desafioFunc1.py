import unittest

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from desafiosObligatorios.desafioFunc1 import tiempoDeDegradacion

class TestDesafioFunc1(unittest.TestCase):

    def test_tiempo_de_degradacion(self):
        tipo=1

        tardaEnDegradar= tiempoDeDegradacion(tipo)

        self.assertEqual(tardaEnDegradar, 150)

if __name__ == "__main__":
    unittest.main()