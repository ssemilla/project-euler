#!/usr/bin/env python

from utils import sieve_arr

prime = sieve_arr(9999)

n = 9
while n < len(prime):
    n = n + 2
    if not prime[n]:
        gold = False
        for root in range(1, n):
            p = n - root*root*2
            if p > 1 and prime[p]:
                gold = True
                break
        if not gold:
            break

print n
                


