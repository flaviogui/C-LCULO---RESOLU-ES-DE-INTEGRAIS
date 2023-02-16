from math import *

def trapezio(f,a,b,n):
    h = (b-a) / n
    soma = 0
    for i in range(1, n):
        soma += f(a+i*h)
    soma *= 2
    soma += (f(a)+f(b))
    return (h / 2) * soma