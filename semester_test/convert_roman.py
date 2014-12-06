#!/usr/bin/env python3

import sys
x = int(sys.argv[1])
#x = int(input())

memo = {'IV':4, 'IX':9}
romandict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

def convert_roman(x):
    romanx = ''
    if x > 1000:
        return 'M'*(x // 1000) + convert_roman(x % 1000)
    if x > 100:
        if x // 100 < 4:
            return 'C'*(x // 100) + convert_roman(x % 100)
        if x // 100 == 4:
            return 'CD' + convert_roman(x % 100)
        if x // 100 == 5:
            return 'D' + convert_roman(x % 100)
        if x // 100 < 9:
            return 'D' + 'C'*(x // 100) + convert_roman(x % 100)
        if x // 100 == 9:
            return 'CM' + convert_roman(x % 100)
    if x > 10:
      if x // 10 < 4:
          return 'X'*(x // 10) + convert_roman(x % 10)
      if x // 10 == 4:
          return 'XL' + convert_roman(x % 10)
      if x // 10 == 5:
            return 'L' + convert_roman(x % 100)
      if x // 10 < 9:
            return 'L' + 'X'*(x // 10) + convert_roman(x % 10)
      if x // 10 == 9:
            return 'XC' + convert_roman(x % 10)
    else:
        if x == 9:
            return 'IX'
        if x > 5:
            return 'V' + 'I'*x
        if x == 4:
            return 'IV'
        if x < 4:
            return 'I'*x

print(convert_roman(x))

