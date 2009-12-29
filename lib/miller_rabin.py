from random import randint


def try_composite(a, d, n, s):
    '''Test the base a to see whether it is a witness for the compositeness
    of n.'''

    if pow(a, d, n) == 1:
        return False

    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False

    # n is definitely composite.
    return True


def is_probable_prime(n, trials=5):
    """Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """

    assert n >= 2

    if n in (2, 3):
        return True

    if n in small_primes:
        return True

    # All primes above 3 have a modulo of 1 or 5.
    if n%6 not in (1, 5):
        return False

    # Quick Sieve of Eratosthenes test for small n's.
    for prime in small_primes:
        if not n%prime:
            return False

    # Write n-1 as 2^s * d
    # Repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    assert(2**s * d == n-1)

    for i in range(trials):
        a = randint(2, n-1)
        if try_composite(a, d, n, s):
            return False

    # No base tested showed n as composite, n is probably prime.
    return True


def gen_primes():
    for prime in small_primes:
        yield prime

    i = small_primes[-1]
    while True:
        i += 2
        if is_probable_prime(i):
            yield i


# To avoid as much hard-coding as possible generate the small_primes list.
small_primes = []
for i in range(2, 100):
    if is_probable_prime(i):
        small_primes.append(i)
