import pandas as pd #libreria para un mayor manejo de archivos csv
from pandas.core.arrays import boolean

info = [] #aqui se almacenan los datos del contacto

def menu(): #funcion menu que inicializa toda la agenda
    print("Bienvenidx a tu agenda virtual\nRecuerda presionar 4 para salir y guardar tus cambios")
    print("Que operacion vas a realizar")
    print("1. Crear un nuevo contacto")
    print("2. Buscar un contacto")
    print("3. Ver todos tus contactos")
    print("4. Para salir")
    opcion = int(input("Ingresa tu opcion > "))

    if opcion == 1: #condicionales para activar las demas funciones
        info.append(crear_contacto())
        input("Contacto guardado, presiona enter para regresar al menu ")
        menu()
    elif opcion == 2:
        buscar_contacto()
        input("Busqueda finalizada, presiona enter para regresar al menu ")
        menu()
    elif opcion == 3:
        listar_contactos()
        input("Esta es la lista de contactos, presiona enter para regresar al menu ")
        menu()
    elif opcion == 4: #guarda la informacion de la variable info en el archivo csv
        df = pd.DataFrame(info, columns=['nombre(s)', 'apeidos', 'direccion', 'email', 'telefono'])
        df.to_csv('agenda.csv')
        print("Vuelve pronto")

def crear_contacto(): #agrega los datos a la variable contacto, regresa esta variable y se alamecena en info
    contacto = []
    contacto.append(input("Ingresa el/los nombre(s) del contacto: "))
    contacto.append(input("Ingresa los apeidos del contacto: "))
    contacto.append(input("Ingresa la direccion de tu contacto: "))
    contacto.append(input("Ingresa el email de tu contacto: "))
    contacto.append(input("Ingresa el numero de tu contacto: "))
    return contacto

def buscar_contacto(): #realiza la busqueda del contacto
    busqueda = input("Ingresa el nombre de tu contacto: ")
    datos = pd.read_csv('agenda.csv') #lee el archivo csv
    df = pd.DataFrame(datos) #crea un dataframe para hacer mas accesible la busqueda
    nombre = df['nombre(s)'] == busqueda #en el campo nombre compara donde se encuentra la variable busqueda, devuelve la posicion y true o false
    resultado = df[df['nombre(s)'] == busqueda] #muestra la fila donde estan los datos
    muestra = resultado[['nombre(s)','apeidos','direccion','email','telefono']].copy() #agrega los campos que mostrara
    filas = len(df.index) #lee la cantidad de filas 
    for i in range(filas):
        if nombre[i] == True: #si encuentra el valor true imprime la fila y termina el bucle
            print(muestra)
        elif nombre[i] == False: #si no hay resultado muestra mensaje y rompe el bucle
            None
        else:
            print("No encontre nada")
    

def listar_contactos(): #lista los contactos con su informacion trayendo los datos de la variable contacto que esta en info
    for contacto in info:
        print("Nombre(s): ", contacto[0])
        print("Apeidos: ", contacto[1])
        print("Direccion: ", contacto[2])
        print("Email: ", contacto[3])
        print("Telefono: ", contacto[4])
        print("--------------------------")
    return

dtmp = pd.read_csv('agenda.csv') #abre y lee el archivo csv
tmp = dtmp.values.tolist() #lista los valores 
for lin in tmp: #evalua las lineas en tmp
    t=[] #guarda los datos en esta variable 
    t.append(lin[1])
    t.append(lin[2])
    t.append(lin[3])
    t.append(lin[4])
    t.append(lin[5])
    info.append(t) #agrega t a la variable info para guardarlo en el csv

menu()