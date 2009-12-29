#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 4 ==============================================================
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# ============================================================================

l = 0
for j in xrange(100, 1000):
    for k in xrange(100, 1000):
        p = j*k
        s = str(p)
        if s != s[::-1]:
            continue

        if p > l:
            l = p

print l
