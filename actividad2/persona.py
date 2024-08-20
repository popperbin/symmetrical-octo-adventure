class persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad
    
    def __getattribute__(self, name: str) -> Any:
        pass
    
        


        
