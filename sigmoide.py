from math import e

def sigmoid(x):
  return 1 / (1 + e**(-x))

print("Ingresa un dato numerico: ")
x=int(input())
print(sigmoid(x))
