import unittest
import app


class Test_app1(unittest.TestCase):
    def test_generar_lista_numeros_con_coma1(self):
        self.assertEqual(
            app.generar_lista_numeros_con_coma('4,5,1,4,7'), 
            ['4', '5', '1', '4', '7'])
            
    def test_generar_lista_numeros_con_coma2(self):
        self.assertEqual(
            app.generar_lista_numeros_con_coma('0,0,0'), ['0', '0', '0'])

    def test_generar_lista_numeros_con_coma3(self):
        self.assertEqual(
            app.generar_lista_numeros_con_coma('12'), ['12'])
    
    def test_generar_lista_numeros_con_coma4(self):
        self.assertEqual(
            app.generar_lista_numeros_con_coma(''), [''])


class Test_app2(unittest.TestCase):
    def test_generar_lista_entera1(self):
        self.assertEqual(
            app.generar_lista_entera(['4', '5', '1', '4', '7']),
            [4, 5, 1, 4, 7])

    def test_generar_lista_entera2(self):
        self.assertEqual(
            app.generar_lista_entera(['0', '0', '0']), [0, 0, 0])
    
    def test_generar_lista_entera3(self):
        self.assertEqual(
            app.generar_lista_entera(['12']), [12])

    def test_generar_lista_entera4(self):
        self.assertEqual(
            app.generar_lista_entera(''), [])


class Test_app3(unittest.TestCase):
    def test_ordenamiento_lista_descendente1(self):
        self.assertEqual(
            app.ordenamiento_lista_descendente([4, 5, 1, 4, 7]),
            [7, 5, 4, 4, 1])

    def test_ordenamiento_lista_descendente2(self):
        self.assertEqual(
            app.ordenamiento_lista_descendente([0, 0, 0]), [0, 0, 0])
    
    def test_ordenamiento_lista_descendente3(self):
        self.assertEqual(
            app.ordenamiento_lista_descendente([12]), [12])

    def test_ordenamiento_lista_descendente4(self):
        self.assertEqual(
            app.generar_lista_entera([]), [])

if __name__ == '__main__':
    unittest.main()
