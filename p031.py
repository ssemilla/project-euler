#!/usr/bin/env python

def c_count(denoms, amt):
    if amt < 0 or len(denoms) == 0:
        return 0
    if amt == 0:
        return 1

    return c_count(denoms, amt - denoms[-1])\
        + c_count(denoms[:-1], amt)

print c_count([1, 2,5,10,20,50,100,200], 200)
