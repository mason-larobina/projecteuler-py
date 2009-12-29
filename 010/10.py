#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 10 =============================================================
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# ============================================================================

from sys import path; path.append('../lib/')
from miller_rabin import is_probable_prime as is_prime

total = 2
for i in xrange(3, int(2e6), 2):
    if is_prime(i):
        total += i

print total
