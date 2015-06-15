
import math

def sieve_arr(limit):
    prime = [True]*limit
    prime[0] = prime[1] = False
    i = 2
    while i < limit:
        if prime[i]:
            j = i + i
            while j < limit:
                prime[j] = False
                j = j + i
        i = i + 1
    return prime

def sieve(limit):
    prime = sieve_arr(limit)
    return lambda x: prime[x]

def sum_divisors(a):
    sqrt_a = int(math.sqrt(a))
    sum = 1
    divisor = 2
    while divisor <= sqrt_a:
        if a % divisor == 0:
            sum = sum + divisor + (a/divisor)
        divisor = divisor + 1
    if sqrt_a**2 == a: sum = sum - sqrt_a
    return sum
