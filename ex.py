diccionario = {
    'Coca':{'stok':3, 'money':10}, 
    'Manzana':{'stok':2, 'money':8}
    }

class Menu:
    def __init__(self, venta):
        self.venta = venta

    def vender(self):
            print ("Actualmente tengo")
            print ("[1] Coca")
            print ("[2] Manzana")
            opcion = input ("Que producto deseas, dime tu elección... ")
            opcion = int(opcion)

            if opcion == 1:
                print ("El costo es de 10 pesos")
                dinero = input("Introduce tú dinero... ")
                dinero = int(dinero)
                
                if dinero >= 20:
                        print ("No tengo cambio")
                        print ("Recuerda pagar con cambio")
                else:
                    num_1= dinero
                    num_2= int(num_1) - 10
                    if num_2 == 0:
                        print ("Difruta tu refresco")
                    else:
                        print ("Toma tu cambio {0}".format(num_2))
                        print ("Difruta tu refresco")
            if opcion == 2:
                print ("El costo es de 8 pesos")
                dinero = input("Introduce tú dinero... ")
                dinero = int(dinero)
                
                if dinero >= 20:
                        print ("No tengo cambio")
                        print ("Recuerda pagar con cambio")
                else:
                    num_1= dinero
                    num_2= int(num_1) - 8
                    if num_2 == 0:
                        print ("Difruta tu refresco")
                    else:
                        print ("Toma tu cambio {0}".format(num_2))
                        print ("Difruta tu refresco")


class MenuAdmin:
    def __init__(self, costos, stoks):
        self.costos=costos
        self.stoks=stoks  

    def ad(self):
        print ("Buen día" "\n"
            "Aqui podras realizar la modificacion de la maquina" "\n")
        print("[1] Cambiar el costo de producto.")
        print("[2] Ingresar producto.")
        opcion = input ("Selecciona que deseas hacer: ")
        opcion = int(opcion)
        if opcion == 1:
                print(self.costo())

        if opcion == 2:
                print(self.stok())
        else:
                print("No existe la selección")

    def costo(self):
        print("Selecciona a que prodcto le quieres Cambiar el costo?")
        print ("[1] Coca")
        print ("[2] Manzana")
        opcion = input("Introduce la opcion... ")
        opcion = int(opcion)
        if opcion == 1:
                #A qui realizas la funcion de Cambiar el costo
                presio = input ("Cual es el nuevo costo ")
                presio = int(presio)
                diccionario ['Coca'] ['money'] = presio
                c = presio
                print ("El nuevo costo es {0}".format(c))
        if opcion == 2:
                presio = input ("Cual es el nuevo costo ")
                presio = int(presio)
                diccionario ['Manzana'] ['money'] = presio
                p = presio
                print ("El nuevo costo es {0}".format(p))
        else:
            return

    def stok(self):
        print("Selecciona a que prodcto le quieres agregar?")
        print ("[1] Coca")
        print ("[2] Manzana")
        opcion = input("Introduce la opcion... ")
        opcion = int(opcion)
        if opcion == 1:
            #A qui realizas la funcion de agregar en el stok
            agrega = input ("Dame la cantidad ")
            agrega = int(agrega)
            valor = diccionario['Coca'] ['stok']
            en = int(valor) + int(agrega)
            diccionario ['Coca'] ['stok'] = en
        if opcion == 2:
            agrega = input ("Dame la cantidad ")
            agrega = int(agrega)
            valor = diccionario['Manzana'] ['stok']
            en1 = int(valor) + int(agrega)
            diccionario ['Manzana'] ['stok'] = en1
            print(en1)
            print (diccionario)
        else:
            pass

class MenuPrincipal (Menu, MenuAdmin):
    def pri(self):
        print ("Buen día" "\n" "A qui esta una maquina de Refrescos" "\n")
        print("[1] Soy un Comprador")
        print("[2] Soy el Administrador")
        opcion = input("Pero quien eres tu ")
        opcion = int(opcion)

        if opcion == 1:
            print(self.op_Menu())
        if opcion == 2:
            print(self.op_Admin())

    def op_Menu (self):
        print(self.vender())

    def op_Admin (self):
        print("Este es el Administrador")
        print(self.ad())

m = MenuPrincipal(0)
m.pri()