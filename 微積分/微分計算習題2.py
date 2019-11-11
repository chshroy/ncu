import pylab
import numpy

pi = pylab.pi
sin = pylab.sin
cos = pylab.cos


def f(x):
    return pylab.sqrt(2*(sin(x)+cos(2*x)+3)/(x+1))
    
def df(x, h):
    return (f(x + h) - f(x)) / h
    
a, b, n = 1, 20, 10000
h = (b - a) / (n - 1)
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))  # draw f(x)
pylab.plot(xs, df(xs, h), color = 'green')
title = "f(x) = sqrt(2(sin(x)+cos(2*x)+3)/(x+1)) and computed derivative"
pylab.title(title, fontsize = 8) # add title

pylab.xlim((0, 20))    # x-axis
pylab.ylim((-1, 2))     # y-axis
pylab.xlabel("x")
pylab.ylabel("y")
pylab.grid()

pylab.show()

