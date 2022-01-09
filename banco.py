import time

class Cola: # Clase que representa una cola
    class _nodo: # Clase que representa un nodo
        def __init__(self, dato):
            self.dato = dato # Dato del nodo
            self.siguiente = None
    def __init__(self): # Constructor
        self.primero = None
        self.ultimo = None
        self.__tam = 0
    def __str__(self): # Metodo que devuelve una cadena con la informacion de la cola
        array = []
        nodo_actual = self.primero
        while nodo_actual != None: # Recorremos la cola
            array.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return str(array)
    def encolar(self, dato): # Metodo que agrega un nodo al final de la cola
        nuevo_nodo = self._nodo(dato)
        if self.primero == None: # Si la cola esta vacia
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.__tam += 1
    def desencolar(self): # Metodo que elimina el primer nodo de la cola
        if self.__tam == 0:
            self.primero = None
            self.ultimo = None 
        else:
            nodo_eliminado = self.primero # Guardamos el nodo a eliminar
            self.primero = nodo_eliminado.siguiente
            nodo_eliminado.siguiente = None
            self.__tam -= 1
            return print(nodo_eliminado.dato)
