from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 1
b = 2
n = 100000

def f(x):
    equacao = 1 / x*(x+1)**2
    return equacao

r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))