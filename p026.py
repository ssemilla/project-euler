#!/usr/bin/env python

# this could be enough
big_10 = 10**10000

def recurring(n):
    length = 1
    while length < len(n):
        if n[-length:] == n[-(length+length):-length]:
            return n[-length:]
        length = length + 1
    return ""
    
longest = (2, 0)
for i in xrange(2, 1000):
    if 1000000 % i:
        long_form = str(big_10 / i)
        recur = recurring(long_form)
        if len(recur) > longest[1]:
            longest = (i, len(recur))

print longest[0]
