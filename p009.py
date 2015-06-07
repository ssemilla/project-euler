#!/usr/bin/env python

ans = None
for a in range(1, 500):
    for b in range(1, 250):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            ans = a*b*c
            break

print ans            
