#!/usr/bin/python3
"""
    AtV3Tjmi4YmpJFX9aSsFAv6GWMsz2yyPua4aJPhTE3pR
"""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
         return list_of_integers[0]

    h = len(list_of_integers) - 1
    1 = 0
    lis = list_of_integers
    while h > l:
         half = (h + l) // 2
         if lis[half] <= lis[half + 1]:
             l = half + 1
         elif lis[half] <= lis[half - 1]:
             h = half - 1
         elif lis[half] >= lis[half + 1] and lis[half] >= lis[half - 1]:
             return lis[half]
    return lis[l]

