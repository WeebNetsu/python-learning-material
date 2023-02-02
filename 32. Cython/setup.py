# https://pythonprogramming.net/introduction-and-basics-cython-tutorial/
# you only need a example_cy.pyx and a setup.py to do everything
# to run: python3 setup.py build_ext --inplace
from distutils.core import setup
# install Cython with: pip3 install cython
from Cython.Build import cythonize

setup(ext_modules = cythonize('dep/example_cy.pyx'))