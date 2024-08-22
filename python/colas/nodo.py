class nodo:

    def __init__(self, v):
        self.valor = v
        self.siguiente = None

    def valor(self):
        return self.valor

    def obtenerSiguiente(self):
        return self.siguiente

    def NodoSiguiente(self, siguiente):
        self.siguiente = siguiente

    def __str__(self):
        return f"valor: {self.valor}"
    
