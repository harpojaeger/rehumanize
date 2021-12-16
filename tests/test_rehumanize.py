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
        (2, "two"),
        (10, "ten"),
        (12, "twelve"),
        (20, "twenty"),
        (95, "ninety-five")])
    def test_s(self, num, string):
        self.assertEqual(rehumanize(num), string)


if __name__ == '__main__':
    unittest.main()
