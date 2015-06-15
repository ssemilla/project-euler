#!/usr/bin/env python

# a * b = c
# c must be 4 digits

from itertools import permutations as perm
from more_itertools import unique_everseen

digits = [c for c in '123456789']

def specials(a_size):
    
    special = []
    for a in perm(digits, a_size):
        
        left = '123456789'
        for d in a: left = left.replace(d, '')
            
        a = int(''.join(a))
    
        for p in perm(left, 5 - a_size):
            b = int(''.join(p))
            product = str(a) + str(b) + str(a*b)

            if b < (9876 / a) and\
               ''.join(sorted(product)) == '123456789':
                special.append(a*b)
                
    return special

print sum(unique_everseen(specials(2) + specials(1)))
