from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = x * (x**2-1)**4
#r = integrate((equacao), (x,1,2)).evalf()
r = Integral((equacao), (x,1,2)).doit()#.evalf()
print("RESULTADO: {} ".format(r))
