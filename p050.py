#!/usr/bin/env python

import utils

prime = utils.sieve_arr(1000000)
prime_len = len(prime)

primes = [x for x in xrange(2, 1000000) if prime[x]]
primes_len = len(primes)
longest = 0
the_prime = 0

for i in xrange(primes_len):
    total = primes[i]

    for j in xrange(i+1, primes_len):
        total = total + primes[j]
        if total >= prime_len:
            break
        else:
            if prime[total] and\
               j - i > longest:
                longest = j - i
                the_prime = total

print the_prime
