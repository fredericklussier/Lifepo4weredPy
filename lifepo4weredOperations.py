#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
reference: lifepo4wered-data.h
"""

import lifepo4weredDefines
from lifepo4weredEnum import lifepo4weredEnum
import lifepo4weredSO

def canRead(what):
    """
    mention if an element can be read.

    :param what: the element to evaluate.
    :type what: Lifepo4weredEnum
    :return: true when read access is available, otherwise false.
    :rtype: bool
    :raises ValueError: if parameter value is not a member of Lifepo4weredEnum.
    """
    if what not in lifepo4weredEnum:
        raise ValueError('Use a lifepo4wered enum element as parameter.')

    return lifepo4weredSO.access_lifepo4wered(what.value, lifepo4weredDefines.ACCESS_READ)

def canWrite(what):
    """
    mention if an element can be written.

    :param what: the element to evaluate.
    :type what: Lifepo4weredEnum
    :return: true when write access is available, otherwise false
    :rtype: bool
    :raises ValueError: if parameter value is not a member of Lifepo4weredEnum
    """
    if what not in lifepo4weredEnum:
        raise ValueError('Use a lifepo4wered enum element as parameter.')

    return lifepo4weredSO.access_lifepo4wered(what.value, lifepo4weredDefines.ACCESS_WRITE)

def read(what):
    """
    read an element from LiFePO4wered.

    :param what: the element to read.
    :type what: Lifepo4weredEnum
    :return: the value of the element
    :rtype: int
    :raises ValueError: if parameter value is not a member of Lifepo4weredEnum
    """
    if what not in lifepo4weredEnum:
        raise ValueError('Use a lifepo4wered enum element as read parameter.')
    
    if canRead(what):
        return lifepo4weredSO.read_lifepo4wered(what.value)
    else:
        raise RuntimeError('You cannot read {0} value, just write it'.format(what.name))

def write(what, value):
    """
    write an element to LiFePO4wered.

    :param what: the element.
    :type what: Lifepo4weredEnum
    :param int value: the value to write.
    :return: the written value
    :rtype: int
    :raises ValueError: if what parameter is not a member of Lifepo4weredEnum
    :raises ValueError: if value is not an int type
    """
    if what not in lifepo4weredEnum:
        raise ValueError('Use a lifepo4wered enum element as write element.')
    
    if isinstance(value, int) is False:
        raise TypeError('Use a int as value.')

    if canWrite(what):
        return lifepo4weredSO.write_lifepo4wered(what.value, value)
    else:
        raise RuntimeError('You cannot write {0} value, just read it'.format(what.name))
