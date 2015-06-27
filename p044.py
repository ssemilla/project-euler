#!/usr/bin/env python

from math import sqrt

# this is just a simplified positive root extraction of 3n^2 -n -2K
def pen_root(K):
    return (1 + sqrt(1 + 24*K)) / 6

def is_pen(K):
    root = int(pen_root(K))
    pen = root * (3 * root -1)
    return pen == K*2

def pen(n):
    return (n * (3 * n - 1)) / 2

    
# now brute force
smallest = pen(9999)
for n in range(1, 9999):
    for k in range(1, n):
        dif = pen(n) - pen(n-k)
        sum = pen(n) + pen(n-k)
        if is_pen(dif) and is_pen(sum):
            if smallest > dif:
                smallest = dif
                
print smallest                
