
def sieve(limit):
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
    return lambda x: prime[x]
