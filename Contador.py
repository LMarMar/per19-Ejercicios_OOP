class Contador():
    def __init__(self, numero):
        self.numero = numero
        self.suma=1
        self.resta = 2
    def get_numero(self):
        return self.numero
    def sumar(self):
        self.numero += self.suma
    def restar(self):
        self.numero -= self.resta

c = Contador(10)
print(c.get_numero())
c.sumar()
c.restar()
print(c.get_numero())
