from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = sin(x)**2
r = integrate((equacao), (x,0,pi/2)).evalf()
print("RESULTADO: {} ".format(r))
