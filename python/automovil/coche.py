class Coche:

    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color         

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.color})"
    
    

        

