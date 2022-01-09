nombre = [] # Lista vacia donde se guardaran los nombres
cantidad = int(input("¿Cuántos nombres ingresarás? ")) # Se pide la cantidad de nombres a ingresar

while cantidad > 0: # Se repite hasta que se ingrese 0
    nombre.append(input("Nombre: ")) # Se ingresa el nombre
    cantidad = cantidad - 1 # Se resta 1 a la cantidad

class persona: # Clase persona
    
    def __init__(self, nombre): # Constructor
        self.nombre = nombre # Se le asigna el nombre
    def eliminar_duplicados(self): # Funcion para eliminar los duplicados
        nombres = set(nombre) # Lista vacia donde se guardaran los nombres no duplicados
        print("Esta es la lista final, elimine todos los datos duplicados" , ', '.join(nombres)) # Se imprime la lista final
lista = persona(nombre) # Se crea una instancia de la clase persona
lista.eliminar_duplicados() # Se llama a la funcion eliminar duplicados
