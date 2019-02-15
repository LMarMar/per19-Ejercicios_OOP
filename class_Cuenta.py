class Cuenta():
    def __init__(self, ingreso = None, transferencia = None, reintegro= None):
        self.ahorros = 3000
        if ingreso is not None:
            self.ingreso = ingreso
        else:
            self.ingreso = 0
        if transferencia is not None:
            self.transferencia = transferencia
        else:
            self.transfencia = 0
        if reintegro is not None:
            self.reintegro = reintegro
        else:
            self.reintegro = 0
        
    def get_ahorros(self):
        return self.ahorros
        
    def ingresar(self):
        self.ahorros += self.ingreso
        return 'Ingreso realizado'
        
    def transferir(self):
        self.ahorros -= self.transferencia
        return 'Transferencia realizada correctamente'
        
    def reintegrar(self):
        self.ahorros -= self.reintegro
        return 'Ha realizado un reintegro'
    
c = Cuenta(100, 80, 40)
print(c.get_ahorros())
print(c.ingresar())
print(c.get_ahorros())
print(c.transferir())
print(c.get_ahorros())
print(c.reintegrar())
print(c.get_ahorros())
