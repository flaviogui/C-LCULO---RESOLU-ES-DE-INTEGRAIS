from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 0
b = 2
n = 1000

def f(x):
    equacao = (4-x**2)**(1/2)
    return equacao



r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))