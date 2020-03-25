import pylab
import numpy
import math
def taylor_poly(n, x):
    s = 0
    for k in range(0, n + 1):
        s = s + ( (-1)**pylab.floor(k/2) * x**(k) ) / math.factorial(k)
    return s
    
def f(x):
    return numpy.sin(x) + numpy.cos(x)

pylab.figure(figsize=(7.5, 4))
a, b, m = 0, 3*numpy.pi, 100
xs = numpy.linspace(a, b, m)
n = 11
for i in range(1, n):
    ys = taylor_poly(i*2-1,xs)
    pylab.plot( xs, ys, label='P'+str(i*2-1) )

pylab.plot( xs, f(xs), label='sin(x)+cos(x)' )
title = 'Taylor polynomials with different orders for sin(x)+cos(x)'
pylab.title(title, fontsize = 8) # add title
pylab.legend(fontsize=6)
pylab.grid()
pylab.xlim(-0.5, 10)    # x-axis
pylab.ylim(-2.0, 2.0)     # y-axis
pylab.xlabel('X')
pylab.ylabel('Y')

pylab.show()
