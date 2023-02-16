from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = 1 / (x**2)+4

r = integrate((equacao), (x,0,2)).evalf()
print("RESULTADO: {} ".format(r))