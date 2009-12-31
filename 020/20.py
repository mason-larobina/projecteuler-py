#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 20 =============================================================
# n! means n * (n - 1) * ... * 3 * 2 * 1
#
# Find the sum of the digits in the number 100!
# ============================================================================

t = 1
for i in xrange(1, 101):
    t *= i

print sum(map(int, str(t)))
