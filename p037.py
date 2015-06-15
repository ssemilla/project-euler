#!/usr/bin/env python

import utils

prime = utils.sieve_arr(1000000)

curious = []

R = [2,3,5,7]
L = [2,3,5,7]

power = 1
while len(curious) < 11:
    R_new = []
    L_new = []
    base = 10**power
    for i in range(base, base * 10):
        if prime[i]:
            R_true = False
            L_true = False
            if (i / 10) in L:
                L_new.append(i)
                L_true = True
            if (i % base) in R:
                R_new.append(i)
                R_true = True
            if R_true and L_true:
                curious.append(i)

    R = R_new
    L = L_new
    power = power + 1
    
print sum(curious)
