import math

def f(x):
    return (x-3.6)+(math.cos(x+1.2))**3

def df(x):
    return 1-3*math.cos(x+1.2)**2 * math.sin(x+1.2)
    

x=0.5

x= x-f(x)/df(x)

print(round(x,5))
