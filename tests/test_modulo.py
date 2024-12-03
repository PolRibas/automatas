import unittest
from src.mi_proyecto.modulo import main

class TestModulo(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main())

if __name__ == '__main__':
    unittest.main()
