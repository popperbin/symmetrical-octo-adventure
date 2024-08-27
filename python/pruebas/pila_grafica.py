from nodopila import Cola

class colaGrafica(Cola):

    def __init__(self, x1, y1, ancho, alto):

        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.ancho = ancho
        self.alto = alto
        