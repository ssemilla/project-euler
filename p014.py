#!/usr/bin/env python

history = {1:1}

def seq_len(n):
    if n == 1: return 1
    if history.has_key(n): return history[n]
    if n % 2:
        history[n] = 1 + seq_len(3*n + 1)
    else:
        history[n] = 1 + seq_len(n / 2)
    return history[n]

longest_i = 1
longest_seq = 1
for i in xrange(2, 1000000):
    i_seq_len = seq_len(i)
    if i_seq_len > longest_seq:
        longest_i = i
        longest_seq = i_seq_len

print longest_i        
