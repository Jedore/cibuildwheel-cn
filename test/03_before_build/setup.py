from setuptools import setup, Extension
import sys

# here we assert that the Python version as written to version.txt in the CIBW_BEFORE_BUILD step
# is the same one as is currently running.
if sys.argv[-1] != '--name':
    with open('pythonversion.txt') as f:
        stored_version = f.read()
    print('stored_version', stored_version)
    print('sys.version', sys.version)
    assert stored_version == sys.version

setup(
    name="spam",
    ext_modules=[Extension('spam', sources=['spam.c'])],
    version="0.1.0",
)
