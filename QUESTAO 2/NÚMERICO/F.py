from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 1
b = 2
n = 1000

def f(x):
    equacao = x * (x**2-1)**4
    return equacao



r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))
