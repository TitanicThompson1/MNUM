"""
dy/dx = z

dz/dx = -By + Az

h é descoberto vendo a variação de x. Com xn+1 = xn + h, entao xn+1 - xn = h. Neste caso concreto, h = 1.6-1.2 = 0.4
"""


def f(x, y, z):
    return z


def fz(x, y, z):
    return -2*y - 8*z

def euler(x, y, z, h):
    for i in range(4):
        print(x, y, z)
        ya = y
        y += f(x, y, z)*h
        z += fz(x, ya, z)*h
        x += h


euler(0.8, 2, 0, 0.4)
