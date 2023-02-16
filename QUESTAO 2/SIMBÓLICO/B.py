from sympy import * 


print("CALCULANDO INTEGRAL SIMBOLICAMENTE")
x = Symbol('x')
#equacao = (x + 4)**(1/2)
equacao = sqrt(x+4)
r = integrate((equacao), (x,-1,4)).evalf()
print("RESULTADO: {} ".format(r))
