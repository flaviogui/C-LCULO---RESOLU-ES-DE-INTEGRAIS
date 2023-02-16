from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = sqrt(3*x+5)

r = integrate((equacao), (x,0,2)).evalf()
print("RESULTADO: {} ".format(r))

