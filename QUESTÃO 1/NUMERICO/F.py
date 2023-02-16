from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 1
b = 4
n = 10000

def f(x):
    equacao = 3*sin(x)
    return equacao

r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))