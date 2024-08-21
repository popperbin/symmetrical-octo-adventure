class nodo():

    def __init__(self, v):
        self.valor = v
        self.siguiente = None

    def NodoSiguiente(self, sig):
        self.siguiente = sig

    def obtenerValor(self):
        return self.valor
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def modificarValor(self, va):
        self.valor = va
        return self.valor
    
 


