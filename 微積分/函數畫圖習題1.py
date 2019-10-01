import pylab
import numpy

def f(x):
    return pylab.maximum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))
    
def g(x):
    return pylab.minimum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))

pi = pylab.pi
a, b, n = -2 * pi, 2 * pi, 10000
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))  # draw f(x)
pylab.plot(xs, g(xs))  # draw g(x)
title = "f(x)=max( abs(x sin(x)), abs(x cos(x)) ), g(x)=min( abs(x sin(x)), abs(x cos(x)) )"
pylab.title(title, fontsize = 8) # add title

pylab.xlim((-8, 8))    # x-axis
pylab.ylim((0, 7))     # y-axis
pylab.grid()

pylab.show()
