#!/usr/bin/env python

# For this problem, I had to look for a primality test
# that can test for primes more that 10**7
# The sieve is not enough anymore.
# There is a nice article on topcoder
# https://www.topcoder.com/community/data-science/data-science-tutorials/primality-testing-non-deterministic-algorithms/
# From wolfram: http://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
# I based my code from the description in wolfram
# I needed to develop the modulo algorithm since using ** operator is
# getting slow for large exponents
# You can see the reasoning for mr_enough in
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

from utils import miller_rabin

prime = miller_rabin

prime_count = 0
term = 1
dist = 0
while True:
    dist += 2
    for i in range(3): # 4th edge is always a square
        term += dist
        if prime(term):
            prime_count += 1
    term += dist
    total = (dist * 2) + 1
    if prime_count * 10 < total:
        break
        
print dist + 1
