from sympy import * 


print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
equacao = (2*x+1) / sqrt(5*x-1) 

r = integrate((equacao), (x,0,1)).evalf()
print("RESULTADO: {} ".format(r))
