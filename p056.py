#!/usr/bin/env python

# brute force forever

largest = 0

for a in range(100):
    for b in range(100):
        digit_sum = sum([int(d) for d in str(a**b)])
        if digit_sum > largest:
            largest = digit_sum

print largest            


