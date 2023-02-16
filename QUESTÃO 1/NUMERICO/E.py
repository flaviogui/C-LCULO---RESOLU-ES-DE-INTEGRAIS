from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 0
b = 2
n = 10000

def f(x):
    equacao = sqrt(3*x+5)
    return equacao

r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))