import unittest

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))

    def test_negative_number(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-17))

    def test_non_integer_input(self):
        self.assertFalse(is_prime(3.14))
        self.assertFalse(is_prime("17"))
        self.assertFalse(is_prime([17]))

if __name__ == '__main__':
    unittest.main()