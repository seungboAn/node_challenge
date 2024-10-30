import unittest
from run_tests import check_output

class TestGrewChallenge(unittest.TestCase):
    def test_output(self):
        expected_output = ["Hello World"]
        self.assertTrue(check_output(expected_output))

if __name__ == '__main__':
    unittest.main()