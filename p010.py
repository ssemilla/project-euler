#!/usr/bin/env python

from utils import sieve

size = 2000000
prime = sieve(size)
i = 0
sum = 0
while i < size:
    if prime(i): sum = sum + i
    i = i + 1
    
print sum
