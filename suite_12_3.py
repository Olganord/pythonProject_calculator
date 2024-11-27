import unittest
import test_12_1
import test_12_3

runners_test_suite = unittest.TestSuite()

runners_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
runners_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runners_test_suite)
