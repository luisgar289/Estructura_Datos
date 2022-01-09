import time
print("Bienvenid@, elige uno de nuestros sabores de refresco" ) #mensaje de bienvenida
refrescos = ["[0]Manzana","[1]Limon","[2]Uva","[3]Cola","[4]Naranja","[5]Piña","[6]Tuti-Fruti"] #lista de refrescos
time.sleep(1)
print("")
print(', '.join(refrescos)) #se muestra la lista de refrescos 
#se define el valor de cada refresco

refresco = [0,1,2,3,4,5,6] #se crea una lista con los numeros de cada sabor de refresco
#se asigna un precio a cada sabor de refresco
refrescos[0] = 20
refrescos[1] = 15
refrescos[2] = 10
refrescos[3] = 40
refrescos[4] = 25
refrescos[5] = 20
refrescos[6] = 35
print("")
time.sleep(0.5)
sabor = input("Selecciona el sabor de tu eleccion: ") #se solicita el sabor
sabor = int(sabor)
print("")
time.sleep(0.5) #se indica el costo de cada sabor
if sabor == refresco[0]:
    print("El costo de tu refresco es de {0}".format(refrescos[0]))
elif sabor == refresco[1]:
    print("El costo de tu refresco es de {0}".format(refrescos[1]))
elif sabor == refresco[2]:
    print("El costo de tu refresco es de {0}".format(refrescos[2]))
elif sabor == refresco[3]:
    print("El costo de tu refresco es de {0}".format(refrescos[3]))
elif sabor == refresco[4]:
    print("El costo de tu refresco es de {0}".format(refrescos[4]))
elif sabor == refresco[5]:
    print("El costo de tu refresco es de {0}".format(refrescos[5]))
elif sabor == refresco[6]:
    print("El costo de tu refresco es de {0}".format(refrescos[6]))
print("")
time.sleep(0.3)
dinero = input("Introduce tu dinero: ") #se guarda en una variable el dinero que el comprador introduce
dinero = int(dinero)

def cambio(dinero_cambio): #se crea una funcion para el sistema de cambio
    if dinero_cambio >= 100:
        monto = dinero_cambio // 100
        if monto == 1:
            print("Tu cambio es de {0} billete de 100".format(monto))
        else:
            print("Tu cambio es de {0} billetes de 100".format(monto))
    dinero_cambio = dinero_cambio % 100
    if dinero_cambio >= 50:
        monto = dinero_cambio // 50
        if monto == 1:
            print("Tu cambio es de {0} billete de 50".format(monto))
        else:
            print("Tu cambio es de {0} billetes de 50".format(monto))
    dinero_cambio = dinero_cambio % 50
    if dinero_cambio >= 20:
        monto = dinero_cambio // 20
        if monto == 1:
            print("Tu cambio es de {0} billete de 20".format(monto))
        else:
            print("Tu cambio es de {0} billetes de 20".format(monto))
    dinero_cambio = dinero_cambio % 20
    if dinero_cambio >= 10:
        monto = dinero_cambio // 10
        if monto == 1:
            print("Tu cambio es de {0} moneda de 10".format(monto))
        else:
            print("Tu cambio es de {0} monedas de 10".format(monto))
    dinero_cambio = dinero_cambio % 10
    if dinero_cambio >= 5:
        monto = dinero_cambio // 5
        if monto == 1:
            print("Tu cambio es de {0} moneda de 5".format(monto))
        else:
            print("Tu cambio es de {0} monedas de 5".format(monto))

if sabor == 0: #se realiza la operacion para el retorno de cambio
    dinero_cambio = dinero - 20
elif sabor == 1:
    dinero_cambio = dinero - 15
elif sabor == 2:
    dinero_cambio = dinero - 10
elif sabor == 3:
    dinero_cambio = dinero - 40
elif sabor == 4:
    dinero_cambio = dinero - 25
elif sabor == 5:
    dinero_cambio = dinero - 20
elif sabor == 6:
    dinero_cambio = dinero - 35

if sabor == 0: #se crea el sistema de despacho de refresco
    if dinero < 20:
        print("")
        print("Dinero insuficiente, orden cancelada")#se cancela la orden en caso de ser insuficiente el dinero
    elif dinero == 20:
        print("")
        print("Toma tu refresco")#solo se entrega el refresco en caso de ser exacto el dinero
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio") #se entrega el refresco y se llama la funcion de cambio
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 1:
    if dinero < 15:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 15:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 2:
    if dinero < 10:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 10:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 3:
    if dinero < 40:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 40:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 4:
    if dinero < 25:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 25:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 5:
    if dinero < 20:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 20:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))
elif sabor == 6:
    if dinero < 35:
        print("")
        print("Dinero insuficiente, orden cancelada")
    elif dinero == 35:
        print("")
        print("Toma tu refresco")
    else:
        print("")
        print("Aqui tienes tu refresco, en un momento tendras tu cambio")
        time.sleep(1)
        print(cambio(dinero_cambio))