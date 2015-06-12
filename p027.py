#!/usr/bin/env python

import utils

prime = utils.sieve(1200000)

quad = lambda a, b, n: (n**2) + (a*n) + b

def consec_primes(a, b):
    n = 0
    while True:
        if prime(quad(a, b, n)):
            n = n + 1
        else:
            return n

largest = (1, 1, 1)            
for a in xrange(-1000, 1000):
    for b in xrange(-1000, 1000):
        if b % 2 == 0 or\
           b % 3 == 0 or\
           b % 5 == 0:
            pass
        else:
            prime_count = consec_primes(a, b)
            if prime_count > largest[2]:
                largest = (a, b, prime_count)

print largest[0] * largest[1]
