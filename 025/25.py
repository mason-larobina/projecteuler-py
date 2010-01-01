#!/usr/bin/python
# Mason Larobina <mason.larobina@gmail.com>

# === Problem 25 =============================================================
# The Fibonacci sequence is defined by the recurrence relation:
#
#   Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
# ============================================================================

def fibs(a=1, b=1):
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b

i = 0
next_fib = fibs().next
while True:
    i += 1
    fib = next_fib()
    if len(str(fib)) == 1000:
        break

print i
