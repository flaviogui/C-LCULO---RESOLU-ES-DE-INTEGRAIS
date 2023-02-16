from sympy import *

x = Symbol('x')

parte1 = 1 #numerador
parte2 = (x + 1) * sqrt(x**2 + 1) #denominador

r = Integral(parte1/parte2,(x, 0, 0.75)).doit().evalf()
print("RESULTADO = {}".format(r))