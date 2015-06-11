#!/usr/bin/env python

file = open('p022_names.txt', 'r')
entries = file.read()

names = [e[1:-1] for e in entries.split(',')]
names.sort()

def score(name):
    return sum([ord(e) - ord('A') + 1 for e in name])

total = 0
for i in xrange(len(names)):
    total = total + (score(names[i]) * (i+1))

print total    
