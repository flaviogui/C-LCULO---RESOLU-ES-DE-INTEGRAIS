from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = (4-x**2)**(1/2)
r = integrate((equacao), (x,0,2)).evalf()
print("RESULTADO: {} ".format(r))