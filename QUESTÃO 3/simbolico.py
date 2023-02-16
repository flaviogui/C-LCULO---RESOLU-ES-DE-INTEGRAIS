from sympy import * 


print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = (x**2-16)**(1/2)/4

r = integrate((equacao), (x,0,4))#.evalf()
print("RESULTADO: {} ".format(r))
