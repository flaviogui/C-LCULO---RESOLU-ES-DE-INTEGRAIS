from formula_trapezio import *

print("CALCULANDO INTEGRAL NUMERICAMENTE")

a = -1
b = 4
n = 1000

def f(x):
    equacao = (x + 4)**(1/2)
    return equacao



r = trapezio(f,a,b,n)
print("O RESULTADO: {}".format(r))