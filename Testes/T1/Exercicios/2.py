import math

def g(x):
    return math.e**-x

x=1.1

for i in range(0,100):
    x=g(x)

print(x)
