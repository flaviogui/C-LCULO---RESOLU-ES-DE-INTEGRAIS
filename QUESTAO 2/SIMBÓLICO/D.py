from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = 3*sin(x)*cos(x)
r = integrate((equacao), (x,0,pi/2)).evalf()
print("RESULTADO: {} ".format(r))
