#!/usr/bin/env python
import os

# Run this in the directory this file (install.py) exists in to 
# install dependencies

os.chdir("./dependencies/numpy-1.9.2")
os.system("python setup.py build")
os.system("python setup.py install")
os.chdir("../biopython-1.65")
os.system("python setup.py build")
os.system("python setup.py install")
os.chdir("../..")

