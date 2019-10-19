import math

def f(x):
    return math.sin(10*x)+math.cos(3*x)

root=3.26242
a=3.2
b=3.3
m=0.0


while abs((root-m)/root)>0.005:
    m= (a+b)/2
    if f(a)*f(m)<0:
        b=m
    else:
        a=m

print (round((a+b)/2,5))

