import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_PaymentRetursTest import PaymentReturnsTest
from Package2.TC_PaymentTest import PaymentClass

# get all the tests here from the imported files
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentClass)

# Creating Test Suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([sanityTestSuite, functionalTestSuite])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
