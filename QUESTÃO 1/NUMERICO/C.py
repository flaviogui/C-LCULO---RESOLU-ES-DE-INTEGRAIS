from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 0
b = 3
n = 100000

def f(x):
    equacao = x / sqrt(x**2+9)
    return equacao

r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))