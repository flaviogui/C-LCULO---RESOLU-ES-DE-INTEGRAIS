from sympy import * 


print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
parte1 = (sin(x)**2)-4*sin(x)*cos(x)+(3*cos(x)**2)
parte2 = sin(x)+cos(x)
r = Integral((parte1/parte2)).doit().evalf()
print("RESULTADO: {} ".format(r))
