#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='fortnox_cli',
      version='1.0',
      # Modules to import from other scripts:
      packages=find_packages(),
      py_modules=['fortnox_cli'],
      entry_points={
          'console_scripts': [
              'fortnox_cli=fortnox_cli:main'
              ],
          },
      )
