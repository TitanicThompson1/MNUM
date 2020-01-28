def f1(x, y):
    return x**2 - y - 1.2


def f2(x, y):
    return -x + y**2 - 1.0


def f1x(x, y):
    return 2*x


def f1y(x, y):
    return -1


def f2x(x, y):
    return -1


def f2y(x, y):
    return 2*y


def newton(x, y):
    for i in range(3):
        xa = x
        x = x - (f1(x, y)*f2y(x, y) - f2(x, y)*f1y(x, y)) / (f1x(x, y)*f2y(x, y) - f2x(x, y)*f1y(x, y))
        y = y - (f2(xa, y)*f1x(xa, y) - f1(xa, y)*f2x(xa, y)) / (f1x(xa, y)*f2y(xa, y) - f2x(xa, y)*f1y(xa, y))
        print("X:  ", x, "Y:  ", y)


newton(1, 1)

# 2.133333      2.066667
# 1.745801      1.697640
  