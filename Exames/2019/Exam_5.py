import math as m


def f(x):
    return -5*m.cos(x) + m.sin(x) + 10


def aurea(x1, x2):
    b = (m.sqrt(5)-1) / 2
    a = b * b
    x3 = x1 + a * (x2 - x1)
    x4 = x1 + b * (x2 - x1)
    for i in range(2):
        if i == 0:
            print(x1, x2, x3, x4, f(x1), f(x2), f(x3), f(x4))
        if f(x3) > f(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + b*(x4 - x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x3 + b*(x2 - x3)
        print(x1, x2, x3, x4, f(x1), f(x2), f(x3), f(x4))           # ????


aurea(2, 4)

print(3.23606797749979-3.0557280900008412+2.76393202250021-2.4721359549995796)          # amplitude???
