print("Funcion ReLu")

def ReLu(val):
    return max(0.0,val)

print("Introduce un valor entero: ")
val=int(input())
print(ReLu(val))