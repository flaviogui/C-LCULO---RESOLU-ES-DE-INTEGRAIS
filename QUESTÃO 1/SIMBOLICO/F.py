from sympy import * 

print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = 3*sin(x)

r = integrate((equacao), (x,1,4)).evalf()
print("RESULTADO: {} ".format(r))
