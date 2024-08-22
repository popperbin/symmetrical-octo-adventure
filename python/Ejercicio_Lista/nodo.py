from persona import persona
class nodo(persona):

    def __init__(self, persona):
        self.valor = persona
        self.siguiente = None

    def obtenerValor(self):
        return self.valor
    
    def obtenerPersona(self):
        return self.valor

    def obtenerSiguiente(self):
        return self.siguiente

    def NodoSiguiente(self, siguiente):
        self.siguiente = siguiente

    def __str__(self):
        return f"turno: {self.valor}"
    
