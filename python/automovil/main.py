from lista import lista
from coche import Coche

c1 = Coche("ferrari", "rojo", 1977)
c2 = Coche("mazda", "amarillo", 1991)
c3 = Coche("toyota", "blanco", 1986)
c4 = Coche("renault", "gris", 2024)
l = lista()

l.addNodo(c1)
l.addNodo(c2)
l.addNodo(c3)
l.addNodo(c4)
l.getLista()
l.cocheInferior()


