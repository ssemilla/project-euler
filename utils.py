
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

def modulo(n, e, p):
    res = 1
    base = n
    while e:
        if e % 2:
            res = (res * base) % p
        base = (base * base) % p
        e /= 2
    return res % p

mr_enough = [2,3,5,7,11,13,17]
    
def miller_rabin(n, iters=16):

    if n < 2:
        return False
    if n == 2:
        return True
    if n != 2 and n % 2 == 0:
        return False

    s = n - 1
    r = 0
    while s % 2 == 0:
        s /= 2
        r += 1

    def pass_test(a):
        if modulo(a, s, n) == 1:
            return True
        j = 0
        while j < r:
            if modulo(a, (2**j)*s, n) == n-1:
                return True
            j += 1
        return False

    i = 0
    while i < len(mr_enough):
        a = mr_enough[i]
        if a < n:
            if not pass_test(a):
                return False
        else:
            break
        i += 1
        
    return True
