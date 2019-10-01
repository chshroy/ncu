import pylab
import numpy

pi = pylab.pi
cos = pylab.cos
max = pylab.maximum
sqrt = pylab.sqrt

def f(x):
    return (cos(x) * cos(x)) / sqrt(max(1, 2 * x - 1))
    
a, b, n = 0, 10 * pi, 10000
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))  # draw f(x)
title = "f(x) = cos(x)^2/sqrt( max(1, 2x-1) )"
pylab.title(title, fontsize = 8) # add title

pylab.xlim((0, 35))    # x-axis
pylab.ylim((0.0, 1.0))     # y-axis
pylab.grid()

pylab.show()
