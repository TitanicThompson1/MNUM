import math as m


def f(x):
    return m.sqrt(1 + (1.5*m.e**(1.5*x))**2)


def trapezios(a, b, h):
    n = round(abs(a-b) / h)
    total = 0
    for i in range(1, n):
        total += 2*f(a + i*h)
    total += f(a) + f(b)
    total *= h/2

    return total


def simpson(a, b, h):
    n = round(abs(a - b) / h)
    total = 0
    for i in range(1, n):
        if i%2 == 0:
            total += 2 * f(a + i * h)
        else:
            total += 4 * f(a + i * h)
    total += f(a) + f(b)
    total *= h/3
    return total


s1 = trapezios(0, 2, 0.25)
print(s1)

s2 = trapezios(0, 2, 0.25/2)
print(s2)

s3 = trapezios(0, 2, 0.25/4)
print(s3)

Qc = (s2 - s1) / (s3 - s2)
print(Qc)

erro = (s3 - s2) / 3
print(erro)


"""     T               S
h       0.25            0.25
h'      0.125           0.125
h''     0.0625          0.0625
L       19.51436        19.29144
L'      19.34573        19.28952
L''     19.30348        19.28940
Qc      3.99135         15.79333
e       -0.01408        -4.06044e-05
"""