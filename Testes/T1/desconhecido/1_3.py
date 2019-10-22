import math

def f(x):
    return math.exp(0.7*x)-x**2-0.5

a=-1.0
b=0.0
i=0

while i<3:
    m=(a+b)/2
    print(str(a)+" " + str(b)+ " " + str(m)+" " + str(f(a))+" "+ str(f(b))+" "+ str(f(m)))
    if f(a)*f(m)<0:
        b=m
    else:
        a=m
    i=i+1

