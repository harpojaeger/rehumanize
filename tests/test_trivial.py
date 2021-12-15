import os
import sys

# Add this file's parent directory to the py PATH. This should allow us to
# import the module without needing to specify a relative path for it.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import rehumanize


assert rehumanize.five() == 4
