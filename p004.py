#!/usr/bin/env python

palindrome = lambda x: x == (int(str(x)[::-1]))

upper = 999
lower = 100
highest = 0

u = upper
while u >= lower:
    l = lower
    while l <= upper:
        product = u * l
        if palindrome(product) and product > highest:
            highest = product
            upper = u
            lower = l
        l = l + 1
    u = u - 1

print highest
