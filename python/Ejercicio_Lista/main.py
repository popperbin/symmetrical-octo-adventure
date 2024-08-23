import time
from cola import cola
from persona import persona

c1 = persona("mateo", 3, 2014)
c2 = persona("jesus", 5, 1989)
c3 = persona("bolivar", 2, 2024)
c4 = persona("nicochi", 6, 1994)

c = cola()
c.mostrarCola()

c.addCola(c1)
c.addCola(c2)
c.addCola(c3)
c.addCola(c4)
c.verPrimero()
c.verUltimo()
c.personaMayor()

c.atenderPersona()
c.atenderPersona()
c.atenderPersona()
c.atenderPersona()


#se requiere organizar una fila de personas segun el numero de turno dado, 
#por cada persona se debe saber el nombre y el numero de turno.

#realizar un metodo que cuando se atienda una persona pase su nombre a un vector