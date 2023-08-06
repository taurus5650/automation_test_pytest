import sys
from os.path import abspath, dirname

# pytest cli rootdir
package_path = abspath(dirname(dirname(__file__)))
sys.path.insert(0, package_path)
