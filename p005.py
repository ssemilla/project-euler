#!/usr/bin/env python

import operator

def prime_factors(n):

    factors = []
    m = 2
    while m <= n:
        if n % m == 0:
            factors.append(m)
            n = n / m
        else:
            m = m + 1
    return factors


def merge_factors(a, b):
    for n in a:
        if n in b: b.remove(n)
    b.extend(a)

factors = []
for i in range(2, 21):
    i_factors = prime_factors(i)
    merge_factors(i_factors, factors)

print reduce(operator.mul, factors, 1)
