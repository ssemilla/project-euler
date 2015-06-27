#!/usr/bin/env python

from utils import sieve_arr
from sets import Set

prime = sieve_arr(1000000)

def prime_factors(n):
    
    factors = []
    div = 2
    
    while n != 1:
        if prime[n]:
            factors.append(n)
            return Set(factors)
        if prime[div] and  n % div == 0:
            factors.append(div)
            n = n / div
            div = 1
        div = div + 1
    return Set(factors)

    
consec_factors = Set()

n = 2
while True:
    n = n + 1
    factors = prime_factors(n)
    if len(factors) == 4:
        consec_factors.add(factors)
        if len(consec_factors) == 4:
            break
    else:
        consec_factors.clear()

print n-3        
