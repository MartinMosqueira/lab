import unittest
import app


class Test_app(unittest.TestCase):
    def test_histograma_de_enteros1(self):
        self.assertEqual(
            app.histograma_de_enteros([1, 2, 3], '+'), ['+', '++', '+++'])
    
    def test_histograma_de_enteros2(self):
        self.assertEqual(
            app.histograma_de_enteros([0, 0], '+'), ['', ''])

    def test_histograma_de_enteros3(self):
        self.assertEqual(
            app.histograma_de_enteros([3, 3, 3, 3], '*'),
            ['***', '***', '***', '***'])

    def test_histograma_de_enteros4(self):
        self.assertEqual(
            app.histograma_de_enteros([0, 1, 1], '@'), ['', '@', '@'])

    def test_histograma_de_enteros5(self):
        self.assertEqual(
            app.histograma_de_enteros([7], '#'), ['#######'])

    def test_histograma_de_enteros6(self):
        self.assertEqual(
            app.histograma_de_enteros([1, 1, 1, 1, 2, 1], '-'),
            ['-', '-', '-', '-', '--', '-'])

if __name__ == '__main__':
    unittest.main()
