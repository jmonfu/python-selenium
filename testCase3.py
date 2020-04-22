import unittest


def setUpModule():
    print("setup Module")


def tearDownModule():
    print("tear down module")


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("this is login test")

    @classmethod
    def tearDown(self):
        print("this is the logout")

    def test_search(self):
        print("this is search test")

    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

    def test_advancedsearch(self):
        print("this is Advanced search test")

    def test_prepaidRecharge(self):
        print("this is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("this is postpaid recharge test")


if __name__ == '__main__':
    unittest.main()
