import math

def f(x):
    return math.sin(10*x)+math.cos(3*x)

def df(x):
    return 10*math.cos(10*x)-3*math.sin(3*x)

root=3.26242
x=3.2


while abs((root-x)/root) > 0.005:
    
    x=x-f(x)/df(x)
    

print (round(x,5))
