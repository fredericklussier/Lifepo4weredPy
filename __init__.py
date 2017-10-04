#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Wrapper to enable lifepo4wered library to Python.
reference: http://lifepo4wered.com/lifepo4wered-pi3.html
"""

from . import lifepo4weredDefines
from .lifepo4weredEnum import lifepo4weredEnum
from .lifepo4weredOperations import canRead, canWrite, read, write

__author__ = "Frederick Lussier <frederick.lussier@hotmail.com>"
__status__ = "dev"
__version__ = "0.1.0"
__date__ = "september 20th 2017"

__ALL__ = [
    "lifepo4weredDefines", 
    "lifepo4weredEnum", 
    "canRead", 
    "canWrite", 
    "read", 
    "write"]