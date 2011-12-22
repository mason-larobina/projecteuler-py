// (C) Mason Larobina <mason.larobina@gmail.com>
// clang -std=c99 -Wall -o a 28.c && time ./a

#include <stdio.h>
#define SIDE_N 1001

int
main(void)
{
    int total = 1, i = 1;
    for (int skip = 2; skip < SIDE_N; skip += 2)
        for (int j = 0; j < 4; j++)
            total += (i += skip);
    printf("%d\n", total);
    return 0;
}
