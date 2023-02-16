from sympy import *

x = Symbol('x')
parte1 = (sin(x) - cos(x))
parte2 = (sin(x) + cos(x))

r = Integral((((parte1 / parte2))**2*x+1),(x,0,pi/4)).doit().evalf()
print("RESULTADO: {} ".format(r))

