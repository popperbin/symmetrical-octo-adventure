class persona:

    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getTurno(self):
        return self.turno
    
    def setTurno(self, turno):
        self.turno = turno      

    def __str__(self):
        return f"{self.turno} {self.nombre}"
 