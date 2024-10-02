import unittest
from src.calculo import soma

class TesteCalculo(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(2,2),4)
        self.assertEqual(soma(-2,2),0)
