from math import e

def sinh(x):
    return ((e**(x)-e**(-x))/2)

def cosh(x):
    return((e**(x)+e**(-x))/2)

def tanh(x):
    return (sinh(x)/cosh(x))

print("Introduce un valor numerico")
x=x=int(input())
print(tanh(x))