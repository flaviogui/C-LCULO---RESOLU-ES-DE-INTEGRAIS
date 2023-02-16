from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = x / sqrt(x**2+9)

r = integrate((equacao), (x,0,3)).evalf()
print("RESULTADO: {} ".format(r))