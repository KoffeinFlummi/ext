#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "ext-util",
  version = "1.0",
  packages = [],
  scripts = ["scripts/ext"],
  install_requires = [],
  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@gmail.com",
  description = "Extract things without having to worry about parameters.",
  long_description = read("README.rst"),
  license = "MIT",
  keywords = "extract archives archive utility",
  url = "https://github.com/KoffeinFlummi/ext",
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Utilities"
  ]
)
