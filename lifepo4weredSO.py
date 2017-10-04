#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
reference: lifepo4wered-data.h
"""

import ctypes 
import os.path

try:
    lib = ctypes.CDLL(
        '/home/pi/Projects/LifePO4wered-Pi/build/SO/liblifepo4wered.so')
except:
    lib = None

def access_lifepo4wered(eLiFePO4weredVar, access_mask):
    """
    Determine if the specified variable can be accessed in the 
    specified manner (read, write or both)
    """
    return lib.access_lifepo4wered(eLiFePO4weredVar, access_mask)

def read_lifepo4wered(eLiFePO4weredVar):
    """
    Read data from LiFePO4wered/Pi
    """
    return lib.read_lifepo4wered(eLiFePO4weredVar)

def write_lifepo4wered(eLiFePO4weredVar, value):
    """
    Write data to LiFePO4wered/Pi
    """
    return lib.write_lifepo4wered(eLiFePO4weredVar, value)
