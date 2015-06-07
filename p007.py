#!/usr/bin/env python

limit = 1000000
prime = [True]*limit
prime[0] = False
prime[1] = False
i = 2
count = 0
while i < limit:
    if prime[i]:
        j = i + i
        count = count + 1
        while j < limit:
            prime[j] = False
            j = j + i
        if count == 10001:
            break
    i = i + 1

print i
