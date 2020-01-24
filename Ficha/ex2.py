"""
matrix = [[2, -6, -1, -38],
          [-3, -1, 7, -34],
          [-8, 1, -2, -20]]

Pelos metodos iterativos, nao irá convergir. é necessario trocar de linhas: l1<->l3

matrix = [[-8, 1, -2, -20],
          [-3, -1, 7, -34],
          [2, -6, -1, -38]]

Na segunda e terceira linha, os ele. da diag. principal continuam a nao ser os maiores, logo: l2<->l3

matrix = [[-8, 1, -2, -20],
          [2, -6, -1, -38],
          [-3, -1, 7, -34]]

Ja irá convergir
"""


def f(y, z):
    return (-20 + 2*z - y)/(-8.0)


def g(x, z):
    return (-38 + z - 2*x)/-6.0


def h(x, y):
    return (-34 + y + 3*x)/7.0


def gauss_jacobi(x, y, z):
    for i in range(7):
        xa, ya, za = x, y, z
        x = f(ya, za)
        y = g(xa, za)
        z = h(xa, ya)
        print("Jacobi- X:  ", x, "Y:  ", y, "Z:  ", z)


gauss_jacobi(1, 1, 1)

def gauss_seidel(x, y, z):
    for i in range(7):
        x = f(y, z)
        y = g(x, z)
        z = h(x, y)
        print("Seidel- X:  ", x, "Y:  ", y, "Z:  ", z)


gauss_seidel(1, 1, 1)
