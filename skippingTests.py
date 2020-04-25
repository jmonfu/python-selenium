import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("this is your search test")

    @unittest.skip("I am skipping this bcos its not ready yet")
    def test_advancedSearch(self):
        print("this is adv test search")

    @unittest.skipIf(1==1, "Numbers no equal")
    def test_prepaid_recharge(self):
        print("this is prepaid recharge")

    def test_postpaid_recharge(self):
        print("this is post paid recharge")

    def test_logging_by_gmail(self):
        print("this is the logging by email test")

    def test_logging_by_twitter(self):
        print("this is logging by twitter")

if __name__ == '__main__':
    unittest.main
