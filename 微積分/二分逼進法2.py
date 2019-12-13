import math
import pylab

cos = pylab.cos
sin = pylab.sin
pi = pylab.pi

def f(x): 
    return 2 * sin(x) + cos(2 * x)
    
a, b, k = (3 * pi) / 2, 2 * pi, 0
fa, fb = f(a), f(b)
tol = 1.e-5

while True:
    c = (a + b) / 2
    k += 1
    print("{:<2} : r in [ {:<10e} , {:<10e} ]".format(k, a, b), sep="")
    fc = f(c)
    if abs(fc) < tol: break

    if fc * fa < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

print()
