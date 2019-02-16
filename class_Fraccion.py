class Fraccion():
    def __init__(self,num, denom = None):
        self.num = num
        if denom is not None:
            self.denom = denom
        else:
            self.denom = 1

    def sumar(self,otro):
        denominador = self.denom*otro.denom
        numerador = (self.num*otro.denom)+(otro.num*self.denom)

        return numerador,denominador

    def restar(self,otro):
        denominador = self.denom*otro.denom
        numerador = (self.num*otro.denom)-(otro.num*self.denom)

        return numerador,denominador

    def multiplicar(self,otro):
        numerador = self.num * otro.num
        denominador = self.denom * otro.denom

        return numerador,denominador

    def dividir(self,otro):
        numerador = self.num * otro.denom
        denominador = self.denom * otro.num

        return numerador,denominador

class TestFraccion():
    def test_sumar(self):

        f1 = Fraccion(2,3)
        f2 = Fraccion(5,6)

        suma = f1.sumar(f2) #3/2
        return suma

    def test_restar(self):

        f1 = Fraccion(7,5)
        f2 = Fraccion(8,9)

        resta = f1.restar(f2) #23/45
        return resta

    def test_multiplicar(self):

        f1 = Fraccion(5,3)
        f2 = Fraccion(9)

        multiplicacion = f1.multiplicar(f2) #15/1
        return multiplicacion

    def test_dividir(self):

        f1 = Fraccion(6,1)
        f2 = Fraccion(9)

        division = f1.dividir(f2) #2/3
        return division

test = TestFraccion()
print(test.test_sumar())
print(test.test_restar())
print(test.test_multiplicar())
print(test.test_dividir())



