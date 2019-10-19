import math

def f(x):
    return math.sin(10*x)+math.cos(3*x)

root=3.26242
a=3.2
b=3.3
w=0.0


while abs((root-w)/root)>0.005:
    w=(a*f(b)-b*f(a))/(f(b)-f(a))
    if f(a)*f(w)<0:
        b=w
    else:
        a=w

print(w)
    
