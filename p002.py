#!/usr/bin/env python


def fib_sum(limit, filter):

    sum = 0
    a, b = 0, 1
    while b < limit:
        if filter(b): sum = sum + b
        b = b + a
        a = b - a
        
    return sum

print fib_sum(4000000, lambda x: x % 2 == 0)
