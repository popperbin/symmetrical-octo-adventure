from nodopila import Pila

cola = Pila()
if cola.vacio():
    print ("la pila esta vacia")

cola.insertar("a")
cola.insertar("b")
cola.insertar(1)
cola.insertar(2)

print("el contenido de la pila es""\n",cola.imprime())