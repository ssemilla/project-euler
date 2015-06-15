#!/usr/bin/env python

total = 0
for n in xrange(1000000):
    n_s = str(n)
    if n_s == n_s[::-1]:
        nb_s = "{0:b}".format(n)
        if nb_s == nb_s[::-1]:
            total = total + n

print total
