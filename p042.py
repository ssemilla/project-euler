#!/usr/bin/env python

# I'm cheating here, ADMINISTRATION (14 letters) is the longest word
# 14 * 26 = 364

file = open('p042_words.txt', 'r')

triangles = [n*(n+1)/2 for n in range(1, 28)]

entries = file.read()
names = [e[1:-1] for e in entries.split(',')]

count = 0
for name in names:
    if sum([ord(c) - ord('A') + 1 for c in name])\
       in triangles:
        count = count + 1

print count
