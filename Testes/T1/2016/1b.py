
def f(x):
    return (0.613*x-1)/(x-1)

a=1.3
b=2
i=0
m=0.0

while i<100:
    m=(a+b)/2
    if f(a)*f(m)<0:
        b=m
    else:
        a=m
    i=i+1

print((a+b)/2)
            
