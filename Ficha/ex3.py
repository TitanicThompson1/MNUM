# alinea a
import math as m

def f(x):
    return 1 - pow(m.e, -x)


def trapezio(a, b, n):
    h = abs(a-b)/n
    total = 0
    for i in range(1, n):
        total += 2*f(a + i*h)
    total += f(a) + f(b)
    total *= h/2
    print("Total:  ", total)
    return total


# trapezio(0, 4, 4)                     #  2.9378403877797137

# alinea b


def simpson(a, b, n):
    h = abs(a-b)/n
    total = 0
    for i in range(1, n):
        if i%2 == 0:
            total += 2*f(a + i*h)
        else:
            total += 4*f(a + i*h)
    total += f(a) + f(b)
    total *= h/3
    print("Total:  ", total)
    return total


# simpson(0, 4, 4)                      # 3.013449252160272

# alinea c

# para os trapezios

print("Trapezios:")
Ts1 = trapezio(0, 4, 4)
Ts2 = trapezio(0, 4, 8)
Ts3 = trapezio(0, 4, 16)

Qc_T = (Ts2 - Ts1)/(Ts3 - Ts2)              # 3.939087258280466
print("Quociente:  ", Qc_T)

erroT = (Ts3 - Ts2)/3
print("Erro:  ", erroT)                     # 0.005086474879017366

# para simpson
print("\nSimpson:")
Ss1 = simpson(0, 4, 4)
Ss2 = simpson(0, 4, 8)
Ss3 = simpson(0, 4, 16)

Qc_S = (Ss2 - Ss1)/(Ss3 - Ss2)
print("Quociente:  ", Qc_S)                 # 14.638326217007794

erroS = (Ss3 - Ss2)/15
print("Erro:  ", erroS)                     # 2.065540870456554e-05


# alinea d

"""
O passo utilizado é adequado para os dois casos:
    - Para o caso dos trapezios, o quociente de convergencia tinha que ser proximo de 4 
    - Para o caso de Simpson, o Qc tinha de ser proximo de 15
"""


