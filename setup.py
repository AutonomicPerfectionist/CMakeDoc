#!/usr/bin/env python3

import os

from setuptools import setup

version_file = "version.txt"
version = "1.0.0" #Default to 1.0.0 if no version file found
if os.path.isfile(version_file):
    with open(version_file, "r") as f:
        version = f.read().strip()

#This will fail if not requirements.txt found, as it should
with open("requirements.txt", "r") as f:
    dependencies = f.read().split()

setup(
      name = 'CMakeDoc',
      version = version,
      description = 'Documentation Generator for the CMake language',
      author = 'Branden Butler',
      author_email = 'bwtbutler@hotmail.com',
      url = 'https =//github.com/CMakePP/CMakeDoc',
      packages = ['cmakedoc', 'cmakedoc.parser'],
      entry_points = {
        'console_scripts': [
            'cmakedoc = cmakedoc:main',
        ],
      },
      package_data =  {
           "": ["*.g4", "*.interp", "*.tokens"]
      },
      install_requires =  dependencies
)
