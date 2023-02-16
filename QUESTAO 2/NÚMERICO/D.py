from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = 0
b = pi/2
n = 10000000

def f(x):
    equacao = 3*sin(x)*cos(x)
    return equacao



r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))