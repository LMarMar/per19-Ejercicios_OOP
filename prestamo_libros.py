class Libro():
    def __init__(self, titulo, prestamo):
        self.titulo = titulo
        self.dias = 10
        self.prestamo = prestamo
    def dame_info(self):
        info = (self.titulo, self.prestamo,  self.dias)
        return info
    def get_dia_prestamo(self):
        return self.prestamo
    def set_devolucion(self):
        return self.prestamo + self.dias
        
libro = Libro('La sombra del viento', 10)
print('info:')
print(libro.dame_info())
print('Dia del prestamo')
print(libro.get_dia_prestamo())
print('Dia de la devolucion')
print( libro.set_devolucion())
       
