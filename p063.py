#!/usr/bin/env python

# We can only use single digits as a base for the powers
# since 10^n will always yeild n+1 digit number
# 9 should be the highest base but the highest power we need
# to check is 21 since 9^22 is just 21 digits

count = 0
for b in range(1, 10):
    for e in range(1, 22):
        if len(str(b**e)) == e:
            count = count + 1

print count
