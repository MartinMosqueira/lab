import unittest
import app


class Test_app(unittest.TestCase):
    
    def test_suma_de_numeros_repetidos_1(self):
        self.assertEqual(app.suma_de_numeros_repetidos(9), 1107)
        
    def test_suma_de_numeros_repetidos_2(self):
        self.assertEqual(app.suma_de_numeros_repetidos(0), 0)
        
    def test_suma_de_numeros_repetidos_3(self):
        self.assertEqual(app.suma_de_numeros_repetidos(10), 102030)
        
    def test_suma_de_numeros_repetidos_4(self):
        self.assertEqual(app.suma_de_numeros_repetidos(53), 540759)
        
    def test_suma_de_numeros_repetidos_5(self):
        self.assertEqual(app.suma_de_numeros_repetidos(234), 234468702)
        
    def test_suma_de_numeros_repetidos_6(self):
        self.assertEqual(app.suma_de_numeros_repetidos(1), 123)
        
if __name__ == '__main__':
    unittest.main()