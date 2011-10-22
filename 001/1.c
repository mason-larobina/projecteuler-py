// (C) Mason Larobina <mason.larobina@gmail.com>
// clang -std=c99 -Wall -o a 1.c && time ./a

// === Problem 1 ===
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <stdio.h>

int
rsum(int min, int max, int step)
{
    int sum = 0;
    for (int i = min; i < max; i += step)
        sum += i;
    return sum;
}

int
main(void)
{
    printf("%d", rsum(3, 1000, 3) + rsum(5, 1000, 5) - rsum(15, 1000, 15));
    return 0;
}
