from sympy import *

x = Symbol("x")

parte1 = asin(sqrt(x))
parte2 = sqrt(x*(1-x))

r = Integral(parte1 / parte2,(x,0,1)).doit().evalf()
print("RESULTADO: {} ".format(r))


