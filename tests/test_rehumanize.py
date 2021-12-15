import os
import sys
import unittest

# Add this file's parent directory to the py PATH. This should allow us to
# import the module without needing to specify a relative path for it.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import rehumanize


class BasicTest(unittest.TestCase):

  def test_basic(self):
    self.assertEqual(rehumanize.rehumanize(1), "one")


if __name__ == '__main__':
    unittest.main()
