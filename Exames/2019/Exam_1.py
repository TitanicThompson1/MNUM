import math as m


def f(x):
    return m.sin(x) + x**5 - 0.2*x + 1


def bissecao(a, b):
    for i in range(6):

        mid = (b+a) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        print("A:  ", a, "B:  ", b, "Mid:  ", mid)

    return mid

x = bissecao(-1, 0)

root = -0.8417343610266149

print("Erro abs:  ", abs(-0.84375+0.828125))
