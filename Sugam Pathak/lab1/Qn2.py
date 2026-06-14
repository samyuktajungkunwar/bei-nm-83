def f(x):
    return x**3 - x -2
def bisection(f,a,b,limit=1e-6):
    while(b-a)/2 >limit:
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(c)==0:
            return c
        elif f(a)*f(c)<0:
            b=c
        else: a=c
    return (a*f(b)-b*f(a))/(f(b)-f(a))

root = bisection(f, 1, 2)
print("Root:", root)
