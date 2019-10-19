def f(x):
    result=x**3+2*x**2+10*x-17
    return result

def df(x):
    return (3*x**2+4*x+10)

x=0
for i in range(1,3):
    x= x -f(x)/df(x)
    print(x)
