#!/usr/bin/env python

# just brute force

n = 1
while True:
    n = n + 1
    n_2x = str(2*n)
    n_3x = str(3*n)
    n_4x = str(4*n)
    n_5x = str(5*n)
    n_6x = str(6*n)    

    if len(n_2x) == len(n_3x) == len(n_4x)\
       == len(n_5x) == len(n_6x):
        if sorted(n_2x) == sorted(n_3x) == sorted(n_4x)\
           == sorted(n_5x) == sorted(n_6x):
            break

print n            
