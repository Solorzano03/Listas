import math
class Tfiguras:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def setBase(self, base):
        self.__base = base

    def setAltura(self, altura):
        self.__altura = altura

    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self.__altura
    
    def area(self):
        return 0
    
    def perimetro(self):
        return 0
    
    def hipotenusa(self):
        return math.sqrt(self.getBase() ** 2 + self.getAltura() ** 2)
    
class Trectanglo(Tfiguras):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def perimetro(self):
        return 2 * self.getBase() + 2 * self.getAltura()
    
    def area(self):
        return self.getBase() * self.getAltura()
    
class Ttriangulo(Tfiguras):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def perimetro(self):
        return self.getBase() + self.getAltura() + self.hipotenusa()
    
    def area(self):
        return (self.getBase() * self.getAltura()) / 2
    
class Trombo(Tfiguras):
    def __init__(self, base, altura, lado):
        super().__init__(base, altura)
        self.__lado = lado

    def setLado(self, lado):
        self.__lado = lado

    def getLado(self):
        return self.__lado

    def perimetro(self):
        return 4 * self.getLado()
    
    def area(self):
        return (self.getBase() * self.getAltura()) / 2

class Toctoedro(Tfiguras):
    def __init__(self, base, altura, profundidad):
        super().__init__(base, altura)
        self.__profundidad = profundidad
    def setprofundidad(self, profundidad):
        self.__profundidad = profundidad
    def getprofundidad(self):
        return self.__profundidad
    def area(self):
        return 2 * self.getbase() * self.getaltura() + 2 * self.getbase() * self.getprofundidad() + 2 * self.getaltura() * self.getprofundidad()
    def volumen(self):
        return self.getbase() * self.getaltura() * self.getprofundidad()
    

    