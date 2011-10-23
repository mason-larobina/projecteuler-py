// (C) Mason Larobina <mason.larobina@gmail.com>
// clang -Wall -std=c99 -o a 15.c && time ./a

// === Problem 15 ===
// Starting in the top left corner of a 2x2 grid, there are 6 routes (without
// backtracking) to the bottom right corner.
//
// How many routes are there through a 20x20 grid?

#include <stdio.h>

long c[21][21];

long
routes(int x, int y)
{
    if (!c[x][y])
        c[x][y] = (!x || !y) ? 1 : routes(x - 1, y) + routes(x, y - 1);
    return c[x][y];
}

int
main(void)
{
    /* zero cache */
    for (int x = 0; x < 21; x++)
        for (int y = 0; y < 21; y++)
            c[x][y] = 0;

    printf("%ld\n", routes(20, 20));
    return 0;
}
