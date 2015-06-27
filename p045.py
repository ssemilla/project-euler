#!/usr/bin/env python

from math import sqrt

def pen_root(K):
    return (1 + sqrt(1 + 24*K)) / 6

def is_pen(K):
    root = int(pen_root(K))
    pen = root * (3 * root -1)
    return pen == K*2

def hex_root(K):
    return (1 + sqrt(1 + 8*K)) / 4

def is_hex(K):
    root = int(hex_root(K))
    hex = root * (2 * root -1)
    return hex == K

n = 285
while True:
    n = n + 1
    tri = n * (n + 1) / 2
    if is_pen(tri) and is_hex(tri):
        n = tri
        break
        
print n
