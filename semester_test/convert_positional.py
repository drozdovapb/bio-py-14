#!/usr/bin/env python3

import sys
x = sys.argv[1]
base1 = int(sys.argv[2])
base2 = int(sys.argv[3])


def convert_positional(x, base1, base2):
    if base1 == base2:
        return x
    newx = 0
    if base2 > base1:
        for i in range(len(x)):
            newx += int(x[i])*base1**(len(x)-1-i)
        return newx
    else:
        temp = int(x)
        i = 0
        while temp > 0:
            newx += (temp % base2)*base1**i
            temp //= base2
            i += 1
        return newx

#print(convert_positional('1010', 2, 10))
#print(convert_positional('10', 10, 2))

print(convert_positional(x, base1, base2))