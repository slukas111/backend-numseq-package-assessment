"""demo"""

def primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def is_prime(m):
    if m == 2 or m == 3:
        return True
    if m % 2 == 0 or m < 2:
        return False
    for m in range(3, int(m ** 0.5) + 1, 2):
        if m % 1 == 0:
            return False
    return True
print(primes(5003))