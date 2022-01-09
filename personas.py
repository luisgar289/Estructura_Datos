class Persona(): #Clase Persona
    def eliminar(self): #Metodo eliminar
        lista = ["oscar","pedro","jose","oscar","pedro","jose",1,1,2,2,3,3] #Lista de datos
        print("Lista original","\n",lista) #Imprimir lista original
        print("Lista sin duplicados","\n",set(lista)) #Imprimir lista sin duplicados

lista1 = Persona() #Instanciar clase
lista1.eliminar() #Llamar metodo eliminar
