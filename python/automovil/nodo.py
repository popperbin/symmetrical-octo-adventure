class nodo:

    def __init__(self, coche):
        self.coche = coche
        self.siguiente = None

    def obtenerCoche(self):
        return self.coche

    def obtenerSiguiente(self):
        return self.siguiente

    def NodoSiguiente(self, siguiente):
        self.siguiente = siguiente

    def __str__(self):
        return f"coche: {self.coche}"
    
