class TV:
    numTV = 0  

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    @staticmethod
    def getNumTV():
        return TV.numTV

    @staticmethod
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def volumenUp(self):
        self.setVolumen(self.volumen + 1)

    def volumenDown(self):
        self.setVolumen(self.volumen - 1)

    def canalUp(self):
        self.setCanal(self.canal + 1)

    def canalDown(self):
        self.setCanal(self.canal - 1)

    def getPrecio(self):
        return self.precio

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def getCanal(self):
        return self.canal

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def setPrecio(self, precio):
        self.precio = precio
    
    def setControl(self, control):
        self.control = control