class nodopila(object):
    dato = None
    siguiente = None 

class Pila(object):

    def __init__(self):
        self.tope = None

    def reiniciar(self):
        self.tope = None

    def insertar(self, dato):
        nodo = nodopila()
        nodo.dato = dato
        nodo.siguiente = self.tope  
        self.tope = nodo

    def quitar(self):
        if self.tope is None:
            raise IndexError("la pila esta vacia")
        x = self.tope.dato  
        eliminarNodo = self.tope
        self.tope = self.tope.siguiente 
        eliminarNodo.siguiente = None 
        return x
    
    def pila_vacia(self):
        return self.tope is None
    
    def topePila(self):
        if self.tope is not None:
            return self.tope.dato
        else:
            return None
        
    def imprime(self):
        paux = Pila()
        cadena = ""
        while not self.pila_vacia():
            dato = self.quitar()
            cadena += str(dato) +"\n"
            paux.insertar(dato)

        while not paux.pila_vacia():
            dato = paux.quitar()
            self.insertar(dato)
        return cadena
    
    def elementos(self):
        paux = Pila()
        cuenta = 0
        while not self.pila_vacia():
            dato = self.quitar()
            paux.insertar(dato)
            cuenta += 1

        while not paux.pila_vacia():
            self.insertar(paux.quitar())
        return cuenta
