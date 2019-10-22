def f(x,y):
    return x**2-y-1.2

def g(x,y):
    return -x+y**2-0.5

def fx(x,y):
    return 2*x

def fy(x,y):
    return -1

def gx(x,y):
    return -1

def gy(x,y):
    return 2*y

x=1.1
y=1.1
i=0
x1=0.0
y1=0.0

while i<2:
    x1= x - (f(x,y) * gy(x,y) - g(x,y) * fy(x,y)) / (fx(x,y) * gy(x,y)-gx(x,y)*fy(x,y))
    y1= y - (g(x,y) * fx(x,y) - f(x,y) * gx(x,y)) / (fx(x,y) * gy(x,y)-gx(x,y)*fy(x,y))

    x=x1
    y=y1
    
    print("x: " + str(x1) + "  y:" + str(y1))
    i+=1


    
