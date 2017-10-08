#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Wrapper to enable lifepo4wered library to Python.
reference: http://lifepo4wered.com/lifepo4wered-pi3.html
"""

from . import defines
from .variablesEnum import variablesEnum
from .functions import canRead, canWrite, read, write

__author__ = "Frederick Lussier <frederick.lussier@hotmail.com>"
__status__ = "dev"
__version__ = "0.1.0"
__date__ = "september 20th 2017"

__ALL__ = [
    "defines", 
    "variablesEnum", 
    "canRead", 
    "canWrite", 
    "read", 
    "write"]