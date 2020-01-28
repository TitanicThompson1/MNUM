def f(t, T):
    return -0.25*(T - 59)


def euler(t, T, h):
    for i in range(2):
        T += f(t, T)*h
        t += h
    return T


print(euler(2, 2, 0.5))