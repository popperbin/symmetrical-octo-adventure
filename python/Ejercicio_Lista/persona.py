class persona:

    def __init__(self, nombre, turno, anho):
        self.nombre = nombre
        self.turno = turno
        self.anho = anho

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getTurno(self):
        return self.turno  
    
    def setTurno(self, turno):
        self.turno = turno

    def getAnho(self):
        return self.anho
    
    def setAnho(self, anho):
        self.anho = anho
 
    def __str__(self):
        return f"{self.turno} - {self.nombre} - {self.anho}"    