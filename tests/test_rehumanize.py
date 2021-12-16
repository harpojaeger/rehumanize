import os
import sys
import unittest

from parameterized import parameterized
from rehumanize import rehumanize

# Add this file's parent directory to the py PATH. This should allow us to
# import the module without needing to specify a relative path for it.
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class RehumanizeTest(unittest.TestCase):

    @parameterized.expand([
        (0, "zero"),
        (2, "two"),
        (9, "nine")])
    def test_one_digit(self, num, string):
        self.assertEqual(rehumanize(num), string)

    @parameterized.expand([
        (10, "ten"),
        (12, "twelve"),
        (20, "twenty"),
        (42, "forty-two"),
        (87, "eighty-seven"),
        (95, "ninety-five")])
    def test_two_digits(self, num, string):
        self.assertEqual(rehumanize(num), string)

    @parameterized.expand([
        (100, "one hundred"),
        (109, "one hundred and nine"),
        (118, "one hundred and eighteen"),
        (177, "one hundred and seventy-seven")
    ])
    def test_three_digits(self, num, string):
        self.assertEqual(rehumanize(num), string)


if __name__ == '__main__':
    unittest.main()
