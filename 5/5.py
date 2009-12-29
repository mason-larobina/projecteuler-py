#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 5 ==============================================================
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest number that is evenly divisible by all of the numbers
# from 1 to 20?
# ============================================================================

d = []

for x in reversed(range(2, 21)):
    for y in d:
        if not y%x:
            break

    if not d or y%x:
        d.append(x)

m = max(d)
i = 0

while True:
    i += 1
    p = m * i
    for x in d:
        g = p % x
        if g:
            break

    if not g:
        break

print p
