#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 67 =============================================================
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#                              3
#                             7 4
#                            2 4 6
#                           8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt a 15K text file
# containing a triangle with one-hundred rows.

h = open('triangle.txt', 'r'); r = h.read(); h.close()
t = [map(int, l.split()) for l in filter(None, map(str.strip, r.split('\n')))]

# ============================================================================


for h in reversed(range(len(t)-1)):
    for j in range(len(t[h])):
        t[h][j] += max(t[h+1][j:j+2])

print t[0][0]
