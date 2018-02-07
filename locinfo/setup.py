""" setup.py for locinfo.
https://github.com/dedenbangkit/locinfo
python setup.py
"""

from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="locinfo",
    version="0.1.0",
    description="Search location with Google Maps API",
    license="MIT",
    author="dedenbangkit",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
