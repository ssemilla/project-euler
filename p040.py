#!/usr/bin/env python

import operator

powers = []
current = ''
taken = 0
pow = 0
for i in xrange(1, 1000000):
    current = current + str(i)
    if taken + len(current) >= 10**pow:
        powers.append(current[10**pow - taken -1])
        if len(current) >= 10:
            taken = taken + 10
            current = current[10:]
        if len(powers) > 6:
            break
        pow = pow + 1
        
print reduce(operator.mul, [int(i) for i in powers], 1)
