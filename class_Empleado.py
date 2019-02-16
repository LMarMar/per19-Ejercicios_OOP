class Empleado():
    def __init__(self, nombre, apellido, salario, tiempo):
        self.nombre = nombre
        self.apellido = apellido
        self.tiempo = tiempo
        self.salario = salario
        if salario > 3000:
            self.tasa = 0.20
        else:
            self.tasa = 0.10
    def impuestos(self):
        pagar = self.salario * self.tasa
        self.salario -= pagar
        return pagar

    def bonus(self):
        if 5 < self.tiempo <= 10:
            self.bonus = 300

            self.salario += self.bonus
        elif 10 < self.tiempo <=20:
            self.bonus = 500

            self.salario += self.bonus
        elif 20 < self.tiempo:
            self.bonus = 1000

            self.salario += self.bonus
        else:
            self.bonus = 0

    def get_info(self):
        print('Nombre:', self.nombre, 'Apellido:', self.apellido, 'Salario final:',self.salario)
        print('Debido a su salario, debe pagar una tasa de impuestos de:', self.impuestos())
        print('Debdo al tiempo que lleva trabajando en la empresa,recibe un bonus de:', self.bonus)
juan = Empleado('Juan', 'Abad',3500,7)
juan.impuestos()
juan.bonus()
juan.get_info()
print()
maria = Empleado('Maria', 'Salmeron',4000,21)
maria.impuestos()
maria.bonus()
maria.get_info()
print()
ana = Empleado('Ana', 'Albacete',2700,5)
ana.impuestos()
ana.bonus()
ana.get_info()
