from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 1
b = 5
n = 100000

def f(x):
    equacao = x**5
    return equacao



r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))