import unittest

class PaymentClass(unittest.TestCase):
    def test_PaymentInDollars(self):
        print("This is a payment in dollars")
        self.assertTrue(True)

    def test_PaymentInEuros(self):
        print("This is a payment in euros")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main
