#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 7 ==============================================================
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6^(th) prime is 13.

# What is the 10001^(st) prime number?
# ============================================================================

def primes():
    all_primes = [2, 3, 5]
    for prime in all_primes:
        yield prime

    i = all_primes[-1]

    while True:
        i += 2

        # The modulo of a prime above 3 is always 1 or 5.
        if i%6 not in [1, 5]:
            continue

        not_prime = False
        for prime in all_primes:
            if not i%prime:
                not_prime = True
                break

        if not_prime:
            continue

        all_primes.append(i)
        yield i


count = 0
next_prime = primes().next
while count < 10001:
    count += 1
    prime = next_prime()

print prime
