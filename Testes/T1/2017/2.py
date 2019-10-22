def f(x,r,m):
    return 1-(r / x**m)

def df(x,r,m):
    return r*m*x**(-m-1)

r=int(input("r: "))
m=int(input("m: "))
x=int(input("x: "))

while 1 :  #inserir condicao
    x= x -f(x,r,m)/df(x,r,m)

