import pylab
import numpy

pi = pylab.pi
sin = pylab.sin


def f(x):
    return (2 + sin(x / pi)) / (2 - sin(x / pi))
    
def df(x, h):
    return (f(x + h) - f(x)) / h
    
a, b, n = 0, 50, 10000
h = (b - a) / (n - 1)
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))  # draw f(x)
pylab.plot(xs, df(xs, h), color = 'green')
title = "f(x) = (2 + sin(x/pi))/(2 - sin(x/pi)) and computed derivative"
pylab.title(title, fontsize = 8) # add title

pylab.xlim((a, b))    # x-axis
pylab.ylim((-1, 3))     # y-axis
pylab.xlabel("x")
pylab.ylabel("y")
pylab.grid()

pylab.show()
