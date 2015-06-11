#!/usr/bin/env python

# from right to left check which adjacent numbers ij
# such that i < j, pivot on i
# e.g. 1247653
# pivot on 4 since 4 < 7
# re_sort = 7653 -> 3567
# replace = 4
# do_none = 12
# 12 4 3567
# then replace 4 and 5 since 5 is the first number > 4 in 3567
# 12 5 3467

N = [c for c in '0123456789']

def pivot_N(i):
    re_sort = N[i+1:]
    re_sort.sort()
    replace = N[i]
    do_none = N[:i]

    for i in range(len(re_sort)):
        if re_sort[i] > replace:
            n = re_sort[i]
            re_sort[i] = replace
            return do_none + [n] + re_sort
    
for k in xrange(999999):

    for i in range(len(N)-1, 0, -1):
        if N[i] > N[i-1]:
            N = pivot_N(i-1)
            break

print ''.join(N)
