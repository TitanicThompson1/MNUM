def f(x,y):
    return x+y-3
def g(x,y):
    return y**2+x**2-9
def fx(x,y):
    return 1
def fy(x,y):
    return 1
def gx(x,y):
    return 2*x
def gy(x,y):
    return 2*y

x_ant=4.0
y_ant=1.0

x=0.0
y=0.0

solx=3.0
soly=0.0

while (abs((solx-x_ant)/x_ant) > 0.05 and abs((soly-y_ant)/y_ant)) > 0.05:

    x=x_ant-(f(x_ant,y_ant)*gy(x_ant,y_ant)-g(x_ant,y_ant)*fy(x_ant,y_ant))/(fx(x_ant,y_ant)*gy(x_ant,y_ant)-gx(x_ant,y_ant)*fy(x_ant,y_ant))
    y=y_ant-(g(x_ant,y_ant)*fx(x_ant,y_ant)-f(x_ant,y_ant)*gx(x_ant,y_ant))/(fx(x_ant,y_ant)*gy(x_ant,y_ant)-gx(x_ant,y_ant)*fy(x_ant,y_ant))

    y_ant=y
    x_ant=x

print(x,y)
