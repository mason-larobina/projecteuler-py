#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 3 ==============================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
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


num = 600851475143

for prime in primes():
    if not num % prime:
        num /= prime

    if prime > num:
        break

print prime
