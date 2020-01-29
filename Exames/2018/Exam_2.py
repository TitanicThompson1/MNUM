import math as m


def f1(x, y):
    return m.sin(x + y) - m.exp(x - y)


def f2(x, y):
    return m.cos(x + y) - x**2 * y**2


def f1x(x, y):
    return m.cos(x + y) - m.exp(x - y)


def f1y(x, y):
    return m.cos(x + y) + m.exp(x - y)


def f2x(x, y):
    return -m.sin(y + x) - 2*x*y**2


def f2y(x, y):
    return -m.sin(x + y) - 2*x**2*y


def newton(x, y):
    for i in range(2):
        xa = x
        x = x - (f1(x, y) * f2y(x, y) - f2(x, y) * f1y(x, y)) / (f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y))
        y = y - (f2(xa, y) * f1x(xa, y) - f1(xa, y) * f2x(xa, y)) / (f1x(xa, y)*f2y(xa, y) - f2x(xa, y) * f1y(xa, y))
        print(x, y)


newton(0.5, 0.5)
