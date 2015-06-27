#!/usr/bin/env python

def lychrel(n):
    iterations = 0
    while iterations < 50:
        iterations = iterations + 1
        reverse = int(str(n)[::-1])
        n = n + reverse
        if str(n) == str(n)[::-1]:
            return False
    return True

count = 0    
for n in range(1, 10000):
    if lychrel(n):
        count = count + 1

print count
