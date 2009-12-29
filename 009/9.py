#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 9 ==============================================================
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#
#   a^2 + b^2 = c^2
#
# For example,
#
#   3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ============================================================================

from math import sqrt
from sys import exit

found = False
for a in range(1, 1000):
    for b in range(1, 1000):
        c = sqrt(a*a + b*b)
        if a + b + c == 1000:
            print int(a * b * c)
            exit(0)
