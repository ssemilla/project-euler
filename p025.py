#!/usr/bin/env python

a = 0
b = 1

i = 1
while True:
    temp = b
    b = a + b
    a = temp
    i = i + 1
    if len(str(b)) >= 1000:
        print i
        break
