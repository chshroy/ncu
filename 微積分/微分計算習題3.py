import pylab
import numpy

pi = pylab.pi
sin = pylab.sin
cos = pylab.cos


def f(t):
    return 1.2732*sin(2*t)+0.4244*sin(6*t)+0.25465*sin(10*t)+0.18189*sin(14*t)+0.14147*sin(18*t)
    
def df(x, h):
    return (f(x + h) - f(x)) / h
    
a, b, n = -pi, pi, 10000
h = (b - a) / (n - 1)
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs), color = 'blue')  # draw f(x)
pylab.plot(xs, df(xs, h), color = 'green')
title = "sawtooth function approximation and derivative"
pylab.title(title, fontsize = 8) # add title

#pylab.xlim((a, b))    # x-axis
#pylab.ylim((-10, 10))     # y-axis
pylab.xlabel("t")
pylab.ylabel("y")
pylab.grid()

pylab.show()
