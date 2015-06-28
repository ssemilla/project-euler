#!/usr/bin/env python

from fractions import Fraction

count = 0
term = 1 + Fraction(1, 2)    
for i in range(1000):
    if len(str(term.numerator)) > len(str(term.denominator)):
        count += 1
    term = 1 + (1 / (1 + term))

print count    

