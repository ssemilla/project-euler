#!/usr/bin/env python

file = open('p067_triangle.txt')

pyramid = [[int(s) for s in line.rstrip().split(' ')] for line in file.readlines()]

# Just copy the logic from p018.py

for i in range(len(pyramid)-1, 0, -1):
    for j in range(0, len(pyramid[i]) -1):
        pyramid[i-1][j] = pyramid[i-1][j] +\
                          max(pyramid[i][j], pyramid[i][j+1])

print pyramid[0][0]
