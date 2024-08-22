from cola import cola
from persona import persona

c1 = persona("mateo", 3)
c2 = persona("jesus", 5)
c3 = persona("bolivar", 2)
c4 = persona("nicochi", 6)

c = cola()
c.mostrarCola()

c.addCola(c1)
c.mostrarCola()
c.addCola(c2)
c.mostrarCola()
c.addCola(c3)
c.mostrarCola()
c.addCola(c4)

c.verPrimero()
c.verUltimo()
c.sacarNodo()
c.mostrarCola()

#se requiere organizar una fila de personas segun el numero de turno dado, 
#por cada persona se debe saber el nombre y el numero de turno.

#realizar un metodo que cuando se atienda una persona pase su nombre a un vector