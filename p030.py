#!/usr/bin/env python

#note (9**5) * 7 = 413343, which is not even 7 digits

max = (9**5) * 6

def sum_e5(n):
    return sum([d**5 for d in [int(d) for d in str(n)]])

total = 0    
for n in range(2, max):
    if sum_e5(n) == n:
        total = total + n

print total        

