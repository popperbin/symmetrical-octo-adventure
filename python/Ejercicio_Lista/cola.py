from nodo import nodo
from persona import persona
class cola(nodo):

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def vacia(self):
        if(self.inicio == None):
            return True
        else:
            return False
        
    def addCola(self, persona):
        nuevo = nodo(persona)

        if self.vacia():
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.siguiente = nuevo
            self.fin = nuevo
        self.size = self.size + 1

    def mostrarCola(self):
        temp = self.inicio
        if temp == None:
            print("cola vacia")
        else:
            while(temp != None):
                print(temp.valor)
                temp = temp.siguiente

    def verPrimero(self):
        if self.inicio:
            print("Primer",self.inicio.valor)
        else:
            print("cola vacia")

    def verUltimo(self):
        if self.fin:
            print("Ultimo",self.fin.valor)
        else:
            print("cola vacia")

    def sacarNodo(self):
        if not self.vacia():
            self.inicio = self.siguiente
            self.size -= 1
            if self.inicio == None:
                self.fin = None
 
    

