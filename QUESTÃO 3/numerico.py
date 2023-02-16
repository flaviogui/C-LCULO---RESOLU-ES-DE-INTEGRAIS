from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 0
b = 4
n = 1000000

def f(x):
    equacao = (x**2-16)**(1/2)/4
    return equacao

r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))