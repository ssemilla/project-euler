#!/usr/bin/env python

concat_x  = lambda i, N : [str(i * n) for n in range(1, N+1)]

largest = 0
for n in range(9, 1, -1):
    for i in xrange(1, 1000000000):
        digits = [str(i*j) for j in range(1, n+1)]
        digits_str = ''.join(digits)
        digits_int = int(digits_str)
        if digits_int > largest:
            digits_len = len(digits_str)
            if digits_len > 9:
                break
            if digits_len == 9 and \
               ''.join(sorted(digits_str)) == '123456789':
                largest = digits_int

print largest
