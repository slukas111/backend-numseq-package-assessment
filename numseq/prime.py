def primes(num):
    """Returns a list of all prime numbers less than n"""
    prime = []
    for num in range(2, n + 1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            prime.append(num)
    # return prime
    # prime_list = []
    # for number in range(num):
    #     if is_prime(number):
    #         prime_list.append(number)
    # return prime_list



def is_prime(m):
    """Returns a boolean indicating whether `m` is a prime number"""
    if m in primes(m):
        return True
    return False