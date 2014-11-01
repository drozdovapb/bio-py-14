import math

figure_type = input()


if figure_type == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())

    def tri_square(a, b, c):
        semiper = (a + b + c) / 2
        return (semiper * (semiper - a) * (semiper - b) * (semiper - c)) ** 0.5

    sq = tri_square(a, b, c)


if figure_type == "rectangle":
    a = float(input())
    b = float(input())

    def rect_square(a, b):
        return a * b

    sq = rect_square(a, b)


if figure_type == "circle":
    d = float(input())
    
    def circle_square(d):
        return math.pi * (d/2) ** 2

    sq = circle_square(d)

print(sq)
