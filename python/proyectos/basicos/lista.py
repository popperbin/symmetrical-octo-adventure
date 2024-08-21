from nodo import nodo

class lista():
      
    def __init__(self):
        self.cabeza = None
        self.size = 0

    def listaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
        
    def addNodo(self, valor):
        if self.listaVacia():
            self.cabeza = nodo(valor)
        else:
            temp = self.cabeza
            nuevo = nodo(valor)
            nuevo.NodoSiguiente(temp)
            self.cabeza = nuevo
        self.size = self.size + 1
    
    def getLista(self):
        temp = nodo(self.cabeza)
        if temp == None:
            print("lista vacia")
        else:
            while(temp != None):
                print("", temp.obtenerValor())
                temp = temp.obtenerSiguiente()

    def buscarDatos(self, dato):
        temp = self.cabeza
        mensaje = ""
        while( temp != None):
            if temp.obtenerValor() == dato:
                mensaje = "dato encontrado"

            temp = temp.obtenerSiguiente()
        if mensaje == "":
            mensaje = "dato no encontrado"
            return mensaje
        
    def eliminarNodo(self, dato):
        temp = self.cabeza
        temp2 = None
        if temp != None and temp.obtenerValor() == dato:
            self.cabeza = None
        else:
            while( temp != None and temp.obtenerValor() != dato):
                temp2 = temp
                temp = temp.obtenerSiguiente()
            if temp != None:
                temp2.NodoSiguiente(temp.obtenerSiguiente())

        


        
            



        