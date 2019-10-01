import pylab
import numpy

def f(x):
    return pylab.maximum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))
    
def g(x):
    return pylab.minimum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))

a, b, n = -2 * pylab.pi, 2 * pylab.pi, 10000
xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))
pylab.plot(xs, g(xs))
pylab.title("f(x)=max[abs(x sin(x)), abs(x cos(x)) ], g(x)=min( abs(x sin(x)), abs(x cos(x)) )")

pylab.grid()


pylab.show()
