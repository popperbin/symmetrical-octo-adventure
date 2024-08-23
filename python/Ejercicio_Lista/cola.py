from nodo import nodo
from persona import persona
class cola:

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

        if (self.vacia()): 
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo # type: ignore
            self.fin = nuevo

    def mostrarCola(self):
        temp = self.inicio

        while(temp != None):
                print("nombre", temp.obtenerValor().getNombre(),"codigo", temp.obtenerValor().getTurno(), "anho", temp.obtenerValor().getAnho())
                print("_________________")
                temp = temp.obtenerSiguiente()

    def verPrimero(self):
        if self.inicio:
            print("Primero en cola", self.inicio.obtenerValor())
        else:
            print("cola vacia")

    def verUltimo(self):
        if self.fin:
            print("Ultimo en cola", self.fin.obtenerValor())
        else:
            print("cola vacia")

    def sacarNodo(self):
        if not self.vacia():
            self.inicio = self.inicio.siguiente # type: ignore
            if self.inicio is None:
                self.fin = None

    def atenderPersona(self):
        origen = []

        origen.append(self.inicio.obtenerValor().getNombre()) # type: ignore
        self.sacarNodo()

        for i in origen:
            print(i)

    def personaMayor(self):
        if self.vacia():
            print('cola vacia')
            return None
        nombre=""
        mayor = 3000
        temp = self.inicio

        while temp is not None:
            if temp.obtenerValor().getAnho() < mayor:
                nombre= temp.obtenerValor().getNombre()
                mayor = temp.obtenerValor().getAnho() 
            temp = temp.obtenerSiguiente()

        print(f"la persona mayor es: {nombre}")

    def edadAnho(self):
        if self.vacia():
            print('cola vacia')
            return None
        edad=""
        mayor = 2024
        temp = self.inicio

        while temp is not None:
            if temp.obtenerValor().getAnho() < mayor:
                nombre= temp.obtenerValor().getAnho()
                mayor = temp.obtenerValor().getAnho() 
                
            temp = temp.obtenerSiguiente()

        print(f"la persona mayor es: {edad}")