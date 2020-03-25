import pylab
import numpy
import math
def taylor_poly(n, x):
    s = 0
    for k in range(1, n):
        s = s + ( (-1)**(k-1) * x**(2*k) ) / math.factorial(2*k-1)
    return s
    
def f(x):
    return x * numpy.sin(x)

pylab.figure(figsize=(7.5, 4))
a, b, m = -3*numpy.pi, 3*numpy.pi, 100
xs = numpy.linspace(a, b, m)
n = 12
for i in range(2, n):
    ys = taylor_poly(i,xs)
    pylab.plot( xs, ys, label='P'+str(2*(i-1)) )

pylab.plot( xs, f(xs), label='x sin(x)' )
title = 'Taylor polynomials with different orders for x sin(x)'
pylab.title(title, fontsize = 8) # add title
pylab.legend(fontsize=6)
pylab.grid()
pylab.xlim(-7, 7)    # x-axis
pylab.ylim(-6, 2)     # y-axis
pylab.xlabel('X')
pylab.ylabel('Y')

pylab.show()
