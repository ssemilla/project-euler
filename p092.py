#!/usr/bin/env python

from sets import Set

list_1 = Set([1])
list_89 = Set([89])

def end_at_1(n):
    global list_1
    global list_89
    chain = Set([n])
    while True:
        if n in list_1:
            list_1 |= chain
            return True
        elif n in list_89:
            list_89 |= chain
            return False
        n = sum(int(c)**2 for c in str(n))
        chain.add(n)
        
count = 0
for n in xrange(1, 10000000):
    if not end_at_1(n):
        count += 1
        
print count        

# is the union of sets hurting the performance?
