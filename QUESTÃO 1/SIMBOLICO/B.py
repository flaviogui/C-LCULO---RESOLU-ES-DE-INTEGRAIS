from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = 1 / x*(x+1)**2

r = integrate((equacao), (x,1,2)).evalf()
print("RESULTADO: {} ".format(r))