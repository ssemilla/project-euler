#!/usr/bin/env python

from utils import sieve_arr

prime = sieve_arr(9999)

primes = [n for n in xrange(2, len(prime)) if n > 1000 and prime[n]]
primes_len = len(primes)

for i in range(primes_len):

    for j in range(i+1, primes_len-2):
        third = primes[j] + primes[j] - primes[i]
        if third < 9999 and prime[third]:
            primes_i_s = str(primes[i])
            primes_j_s = str(primes[j])
            third_s = str(third)
            if sorted(primes_i_s) == sorted(primes_j_s) == sorted(third_s):
                if primes[i] != 1487:
                    print primes_i_s + primes_j_s + third_s
                    break
            
