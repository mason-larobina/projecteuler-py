#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 48 =============================================================
# The series,
#   1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series,
#   1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).
# ============================================================================

t = 0
for i in xrange(1, 1001):
    t += i**i

print str(t)[-10:]
