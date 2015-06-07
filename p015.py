#!/usr/bin/env python

def count_paths(n):
    n = n + 1
    row = range(1, n+1)
    while row[1] < n:
        for i in range(1, n):
            row[i] = row[i] + row[i-1]
    return row[-1]
    
print count_paths2(20)    
