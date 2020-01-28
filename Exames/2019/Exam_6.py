def f(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def fx(x, y):
    return 6*x - y - 8


def fy(x, y):
    return -y + 11 +2*y


def gradiente(x, y, h):
    for i in range(2):
        print(x, y, f(x, y), fx(x, y), fy(x, y))
        xn = x - h*fx(x, y)
        yn = y - h*fy(x, y)
        if f(xn, yn) < f(x, y):
            h *= 2
        else:
            h /= 2
        x, y = xn, yn


gradiente(2, 2, 0.5)            # como saber qual o melhor lambda?
