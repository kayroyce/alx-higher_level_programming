#!/usr/bin/python2
"""
Contains method lookup that returns list of object's attribute and methods
"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    return dir(obj)
