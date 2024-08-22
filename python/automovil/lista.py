from nodo import nodo
from coche import Coche

class lista:
      
    def __init__(self):
        self.cabeza = None
        self.size = 0

    def listaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
        
    def addNodo(self, coche):
        if self.listaVacia():
            self.cabeza = nodo(coche)
        else:
            temp = self.cabeza
            nuevo = nodo(coche)
            nuevo.NodoSiguiente(temp)
            self.cabeza = nuevo
        self.size = self.size + 1
    
    def getLista(self):
        temp = self.cabeza
        if temp == None:
            print("lista vacia")
        else:
            while(temp != None):
                print(temp.obtenerCoche())
                temp = temp.obtenerSiguiente()

    def cocheInferior(self):
        temp = self.cabeza

        while (temp != None):
            if temp.obtenerCoche().getModelo() < 2015:
                print("los vehiculos menores a 2015 son: ", "\nMarca: ",temp.obtenerCoche().getMarca(),
                       ", Color: ",temp.obtenerCoche().getColor(), " Modelo: ", temp.obtenerCoche().getModelo())
            temp = temp.obtenerSiguiente()
 
           
    def buscarDatos(self, dato):
        temp = self.cabeza
        mensaje = ""
        while( temp != None):
            if temp.obtenerCoche() == dato:
                mensaje = "dato encontrado"

            temp = temp.obtenerSiguiente()
        if mensaje == "":
            mensaje = "dato no encontrado"
            return mensaje
        
        