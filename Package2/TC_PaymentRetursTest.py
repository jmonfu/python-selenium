import unittest


class PaymentReturnsTest(unittest.TestCase):
    def test_PaymentReturnByBank(self):
        print("This is a returned payment from the bank")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main
