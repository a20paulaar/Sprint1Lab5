import unittest
from operaciones import dividir

class TestMultiplicar(unittest.TestCase):
    
 def test_dividir(self):
     
    self.assertEqual(dividir(6, 2), 3)
    self.assertEqual(dividir(-1, 1), -1)
    self.assertEqual(dividir(-2, -1), 2)
    self.assertEqual(dividir(-2, 0), "error")
    
if __name__ == '__main__':
 unittest.main()