def max(a, b):
    """ (number, number) -> number
    returns the larger of two numbers

    >>> max(1, 2)
    2
    >>> max(2/2, 1.00)
    1.0
    """
    if a > b:
        return a
    return b

def min(a, b):
    """ (number, number) -> number
    returns the smaller of two numbers
    >>> min(1, 2)
    1
    >>> min(2/2, 1.00)
    1.0
    """
    if a < b:
        return a
    return b



def sort2(a, b, c):
    if a > b:
        if a > c:
            maxi = a
            medi = c
            mini = b
        maxi = c
        medi = a
        mini = b
    if b > c:
        maxi = b
        medi = c
        mini = a


#step 3

def check(x):
    return x > -15 and x <= 12 or x > 14 and x < 17 or x >= 19

#step 4

first = input()
second = input()
operand = input()

def calc(first, second, operand):
    first = float(first)
    second = float(second)
    if operand == "+":
        return first + second
    if operand == "-":
        return first - second
    if operand == "/":
        return first/second
    if operand == "*":
        return first * second
    if operand == "mod":
        return first % second
    if operand == "pow":
        return first ** second
    if operand == "div":
        return first // second

print(calc(first, second, operand))


#step 5

figure_type = input()

if figure_type == "triangle":
    a = int(input())
    b = int(input())
    c = int(input())

    def tri_square(a, b, c):
        semiper = (a + b + c) / 2
        return (semiper * (semiper - a) * (semiper - b) * (semiper - c)) ** 0.5

    sq = tri_square(a, b, c)


if figure_type == "rectangle":
    a = int(input())
    b = int(input())

    def rect_square(a, b):
        return a * b

    sq = rect_square(a, b)


if figure_type == "circle":
    d = int(input())

    import math
    
    def circle_square(d):
        return math.pi* (d/2)**2

    sq = circle_square(d)

print(sq)
