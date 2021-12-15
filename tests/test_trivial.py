import os
import sys

# Add the relative path to the module to the py PATH. This should allow us to to
# import the module without needing to specify a relative path for it.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import rehumanize


assert rehumanize.five() == 4
