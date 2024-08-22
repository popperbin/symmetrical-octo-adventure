from nodo import nodo

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
        
    def addCola(self, v):
        nuevo = nodo(v)

        if(self.vacia()):
            self.inicio = nuevo
            self.fin = nuevo

        else:
            self.siguiente = nuevo
            self.fin = nuevo

    def mostrarCola(self):
        temp = self.inicio
        if temp == None:
            print("cola vacia")
        else:
            while(temp != None):
                print(temp.valor)
                temp = temp.siguiente

    def verPrimero(self):
        print("Primer",self.inicio)

    def verUltimo(self):
        print("Ultimo",self.fin)

    def sacarNodo(self):
        self.inicio = self.siguiente


    

