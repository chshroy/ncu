import pylab
import numpy

pi = pylab.pi
sin = pylab.sin


def f(x):
    return sin(x) / abs(2 * x)
    
a, b, n = -10 * pi, 10 * pi, 10000
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))  # draw f(x)
title = "f(x) = sin(x)/|2x|"
pylab.title(title, fontsize = 8) # add title

pylab.xlabel("x")
pylab.ylabel("y")
pylab.grid()

pylab.show()
