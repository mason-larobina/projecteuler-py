// (C) Mason Larobina <mason.larobina@gmail.com>
// clang -std=c99 -Wall -o a 17.c && time ./a

#include <stdio.h>

// one -> nineteen
int digits[20] = { 0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8 };

// twenty -> ninety
int tens[10] = { 0, 0, 6, 6, 5, 5, 5, 7, 6, 6 };

int 
main(void)
{
    int count = 11; // one thousand
    for (int i = 1; i < 1000; i++) {
        int hunds = i / 100, tensones = i % 100;
        count += 
            (hunds ? digits[hunds] + 7 : 0) // hundreds
            + (hunds && tensones ? 3 : 0)   // and?
            + tens[tensones / 10]           // twenty -> ninety
            + (tensones < 20 ? 
                    digits[tensones]        // one -> nineteen
                  : digits[tensones%10]);   // one -> nine
    }

    printf("%d\n", count);
    return 0;
}
