#!/usr/bin/env python

from setuptools import setup

setup(name='python-pushsafer',
      version='0.3',
      description="Comprehensive bindings for the "
                  "Pushsafer.com notification service",
      long_description=open("README.rst").read() + "\n"
      + open("AUTHORS.rst").read() + "\n" + open("CHANGES.rst").read(),
      url='https://github.com/appzer/python-pushsafer',
      author='Kevin Siml',
      author_email='info@appzer.de',
      py_modules=['pushsafer'],
      entry_points={"console_scripts": ["pushsafer = pushsafer:main"]},
      install_requires=['requests>=1.0'],
      use_2to3=True,
      license='GNU GPLv3'
      )
