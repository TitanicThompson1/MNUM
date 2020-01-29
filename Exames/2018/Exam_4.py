malha = [[5.7, 1.5, 1.2],
        [2.1, 4.8, 2.2],
        [1.1, 1.4, 6.5]]


def cubatura():
    somatorio1 = malha[0][0] + malha[0][2] + malha[2][0] + malha[2][2]
    somatorio2 = 4*(malha[1][0] + malha[0][1] + malha[1][2] + malha[2][1])
    somatorio3 = 16*(malha[1][1])
    hy = (2-0)/2
    hx = (2-0)/2
    somatorio = somatorio1 + somatorio2 + somatorio3
    somatorio *= (hx*hy/9)
    return somatorio


print(cubatura())