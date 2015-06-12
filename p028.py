#!/usr/bin/env python

sum_sides = lambda base, dist: (base*4) + (dist*10)
next_base = lambda base, dist: base + (dist*4)

base = 1
side = 2

sum = 1
while side <= 1001:
    sum = sum + sum_sides(base, side)
    base = next_base(base, side)
    side = side + 2

print sum    
