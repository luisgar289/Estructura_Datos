import time

class Stack: # Clase que representa una pila
    class _nodo: # Clase que representa un nodo
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None
    def __init__(self): # Constructor
        self.cabeza = None
        self.cola = None
        self.tamano = 0
    def __str__(self): # Metodo que devuelve una cadena con la informacion de la pila
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + " Tamaño " + str(self.tamano) # Retornamos la cadena con la informacion de la pila
    def push(self, valor): # Metodo que agrega un nodo al final de la pila
        nuevo_nodo = self._nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamano += 1
    def pop(self): # Metodo que elimina el ultimo nodo de la pila
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza # Guardamos el nodo a eliminar
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamano -= 1
            return nodo_eliminado.valor # Retornamos el valor del nodo eliminado

