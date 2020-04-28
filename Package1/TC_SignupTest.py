import unittest

class SignupTest(unittest.TestCase):
    def test_SignupByEmail(self):
        print("This is a signup by email test")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("This is a signup by facebook test")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("This is a signup by twitter test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main
