from numpy import where
import pandas as pd
from pandas.core.arrays import boolean
from banco import Cola

info = []
dinero_guardado = []
log = Cola()
administradores = {"Jose" : 12345, "Juan" : 54321, "Pedro" : 67890, "Jorge" : 98765}

dtmp = pd.read_csv('proyecto.csv') #abre y lee el archivo csv
tmp = dtmp.values.tolist() #lista los valores 
for lin in tmp: #evalua las lineas en tmp
    t=[] #guarda los datos en esta variable 
    t.append(lin[1])
    t.append(lin[2])
    t.append(lin[3])
    info.append(t) #agrega t a la variable info para guardarlo en el csv

dtmp2 = pd.read_csv('dinero.csv') #abre y lee el archivo csv
tmp2 = dtmp2.values.tolist()
for lin2 in tmp2:
    t2=[]
    t2.append(lin2[1])
    dinero_guardado.append(t2)

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

def main():
    opcion = int(input("Bienvenido\nElige una opcion:\n 1. Cliente\n 2. Administrador\n->"))
    if opcion == 1:
        print("Cliente")
        cliente()
    elif opcion == 2:
        print("Administrador")
        login()
    else:
        print("Opcion no valida")
        main()

def login():
    print("--------------------------------")
    usuario = input("Ingrese usuario: ")
    clave = int(input("Ingrese clave: "))
    if administradores[usuario] == clave:
        print("Bienvenido", usuario)
        administrador()
        log.encolar(usuario)
    else:
        print("Usuario o clave incorrecta")
        login()

def administrador():
    print("--------------------------------")
    print("1. Agregar Refresco")
    print("2. Editar Refresco")
    print("3. Eliminar Refresco")
    print("4. Mostrar Refrescos")
    print("5. Retirar Dinero")
    print("6. Salir")
    opcion = int(input("Ingrese una opcion: "))
    print("--------------------------------")
    
    if opcion == 1:
        log.encolar("Agregar Refresco")
        info.append(agregar())
        print("Refresco agregado")
        administrador()
    elif opcion == 2:
        log.encolar("Editar Refresco")
        editar()
        administrador()
    elif opcion == 3:
        log.encolar("Eliminar Refresco")
        eliminar()
        administrador()
    elif opcion == 4:
        mostrar()
        administrador()
    elif opcion == 5:
        log.encolar("Retirar Dinero")
        retirar()
        administrador()
    elif opcion == 6:
        df = pd.DataFrame(info, columns=[["Nombre", "Precio", "Cantidad"]])
        df.to_csv('proyecto.csv')
        print("Cambios realizados...")
        print(log)
        print("Saliendo...")
    else:
        print("Opcion no valida")
        main()

def agregar():
    lista = []
    nombre = input("Ingrese nombre: ")
    lista.append(nombre)
    precio = int(input("Ingrese precio: "))
    lista.append(precio)
    cantidad = int(input("Ingrese cantidad: "))
    lista.append(cantidad)
    return lista
        
def editar():
    mostrar()
    nombre = input("Ingrese nombre: ")
    for i in info:
        if i[0] == nombre:
            precio = int(input("Ingrese precio: "))
            cantidad = int(input("Ingrese cantidad: "))
            i[1] = precio
            i[2] = cantidad
            print("Refresco editado")
            break
    else:
        print("Refresco no encontrado")

def eliminar():
    mostrar()
    nombre = input("Ingrese nombre: ")
    for i in info:
        if i[0] == nombre:
            info.remove(i)
            print("Refresco eliminado")
            break
    else:
        print("Refresco no encontrado")

def mostrar():

    for refresco in info:
        print("Nombre: ", refresco[0])
        print("Precio: ", refresco[1])
        print("Piezas: ", refresco[2])
        print("--------------------------------")
    return

def retirar():
    total = 0
    for dinero in dinero_guardado:
        total += dinero[0]
    print("Dinero en caja: ", total)
    retiro = int(input("Ingrese dinero a retirar: "))
    if retiro > total:
        print("No hay suficiente dinero")
        retirar()
    else:
        total -= retiro
        dinero_guardado.clear()
        dinero_guardado.append([total])
        print("Dinero retirado")
        print("Dinero en caja: ", total)
    df2 = pd.DataFrame(dinero_guardado, columns=["Dinero"])
    df2.to_csv('dinero.csv')
 
def cliente():
    print("--------------------------------")
    print("Estos son todos los refrescos disponibles")
    mostrar()
    compra = input("Ingrese el nombre del refresco que desea comprar: ")
    for refresco in info:
        if refresco[0] == compra:
            cantidad = int(input("Cantidad de refrescos: "))
            if refresco[2] >= cantidad:
                print("--------------------------------")
                print("Compra realizada")
                refresco[2] = refresco[2] - cantidad
                print("--------------------------------")
                print("Cantidad disponible: ", refresco[2])
                costo_final = refresco[1] * cantidad
                print("--------------------------------")
                dinero = int(input("Ingrese el dinero: "))
                if dinero >= costo_final:
                    dinero_cambio = dinero - costo_final
                    print("Cambio: ", cambio(dinero_cambio))
                    print("--------------------------------")
                    print("Gracias por su compra")
                    print("--------------------------------")
                    df = pd.DataFrame(info, columns=[["Nombre", "Precio", "Cantidad"]])
                    df.to_csv('proyecto.csv')
                    dinero_guardado.append([costo_final])
                    df2 = pd.DataFrame(dinero_guardado, columns=["Dinero"])
                    df2.to_csv('dinero.csv')
                else:
                    print("Dinero insuficiente")
                    print("--------------------------------")
                    cliente()
                break
            else:
                print("No hay suficientes piezas")
                print("--------------------------------")
                break
    else:
        print("Refresco no encontrado")

main()
