#!/usr/bin/env python

from setuptools import setup

setup(
    name="python-pushsafer",
    version="1.2",
    description="Comprehensive bindings for the " "Pushsafer.com notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/appzer/python-pushsafer",
    author="Kevin Siml",
    author_email="info@appzer.de",
    py_modules=["pushsafer"],
    install_requires=["requests>=1.0"],
    license="GNU GPLv3",
)
