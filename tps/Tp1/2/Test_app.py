import unittest
import app


class Test_app(unittest.TestCase):
    
    def test_suma_de_numeros_repetidos_1(self):
        self.assertEqual(app.suma_de_numeros_repetidos(9, 3), 1107)
        
    def test_suma_de_numeros_repetidos_2(self):
        self.assertEqual(app.suma_de_numeros_repetidos(0, 1), 0)
        
    def test_suma_de_numeros_repetidos_3(self):
        self.assertEqual(app.suma_de_numeros_repetidos(10, 2), 1020)
        
    def test_suma_de_numeros_repetidos_4(self):
        self.assertEqual(app.suma_de_numeros_repetidos(53, 4), 54076112)
        
    def test_suma_de_numeros_repetidos_5(self):
        self.assertEqual(app.suma_de_numeros_repetidos(234, 1), 234)
        
    def test_suma_de_numeros_repetidos_6(self):
        self.assertEqual(app.suma_de_numeros_repetidos(1, 6), 123456)
        
if __name__ == '__main__':
    unittest.main()
