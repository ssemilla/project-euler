#!/usr/bin/env python

import utils

MAX = 100 + 1

prime = utils.sieve(MAX)

def prime_factors(n):
    factors = []
    while not prime(n):
        for i in range(n):
            if prime(i) and n % i == 0:
                factors.append(i)
                n = n / i
                break
    factors.append(n)
    return factors

# prime factor each a/b
factors = [[], []]

for i in range(2, MAX):
    factors.append(prime_factors(i))

def encode(factors, exponent):
    factors = factors[:]
    encoded = ""
    while factors:
        expsum = exponent
        base = factors.pop(0)
        while factors and factors[0] == base:
            expsum = expsum + exponent
            factors.pop(0)
        encoded = encoded + str(base) + 'e' + str(expsum) + '.'
    return encoded

map = {}
    
for a in factors:
    if len(a):
        for b in range(2, MAX):
            key = encode(a, b)
            map[key] = 1
                
print len(map)

