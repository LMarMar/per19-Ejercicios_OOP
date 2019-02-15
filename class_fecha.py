class Fecha():
    def __init__(self, year, mes, dia):
        self.year = year
        self.mes = mes
        self.dia = dia
    
    def get_info(self):
        info = (self.dia,'/',self.mes,'/',self.year)
        return info
   
    def comprobar(self):
        if self.year > 2019:
            return 'EL year es incorrecto'
        elif self.mes > 12:
            return 'Ese mes no existe'
        elif self.dia > 31:
            return 'El dia no es correcto'
        else:
            return 'Fecha correcta'

    def next_day(self):
        self.dia +=1
        if self.dia> 31:
            self.dia = 1
            self.mes +=1
        if self.mes > 12:
           self.mes = 1
           self.year += 1

fecha = Fecha(2019, 2, 4)
print(fecha.get_info())
print(fecha.comprobar())
fecha.next_day()
print(fecha.get_info())
