from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = x**5
#r = integrate((equacao), (x,1,5)).evalf()
r = Integral((equacao),(x,1,5)).doit().evalf()
print("RESULTADO: {} ".format(r))
