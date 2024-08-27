class nodoCola():
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None 

class Cola():

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def reiniciar(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato):
        nodo = nodoCola(dato)
        if self.cola == None:
            self.cabeza = nodo
        else:
            self.cola.siguiente = nodo
        self.cola = nodo


    def quitar(self):
        if self.cabeza == None:
            raise IndexError("la cola esta vacia")
        x = self.cabeza.dato  
        self.cabeza = self.cabeza.siguiente
        if self.cabeza == None:
            self.cola = None
        return x
    
    def cola_vacia(self):
        return self.cabeza == None
    
    def primerCola(self):
        if self.cabeza != None:
            return self.cabeza.dato
        else:
            return None
        
    def imprime(self):
        paux = Cola()
        cadena = ""
        while not self.cola_vacia():
            dato = self.quitar()
            cadena += str(dato) +"\n"
            paux.insertar(dato)

        while not paux.cola_vacia():
            dato = paux.quitar()
            self.insertar(dato)
        return cadena
    
    def elementos(self):
        paux = Cola()
        cuenta = 0
        while not self.cola_vacia():
            dato = self.quitar()
            paux.insertar(dato)
            cuenta += 1

        while not paux.cola_vacia():
            self.insertar(paux.quitar())
        return cuenta
