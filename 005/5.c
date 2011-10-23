// (C) Mason Larobina <mason.larobina@gmail.com>
// clang -std=c99 -Wall -o a 5.c && time ./a

// === Problem 5 ===
// 2520 is the smallest number that can be divided by each of the numbers
// from 1 to 10 without any remainder.
//
// What is the smallest number that is evenly divisible by all of the numbers
// from 1 to 20?

#include <stdio.h>

const int divs[] = {
    20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 0
};

int
main(void)
{
    long n = 20;

    while ((n += 20)) {
        const int *p = divs + 1;
        for (; *p && (n % *p == 0); p++)
            continue;

        if (!*p)
            break;
    }

    printf("%ld\n", n);
    return 0;
}
