class Alumno():
    def __init__(self, matricula, nombre, nota1,nota2,nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        nota_final = (self.nota1 + self.nota2 + self.nota3) /3
    
    def dame_info (self):
        print('Número de matrícula:', self.matricula)
        print('Alumno:', self.nombre)
        
    def nota_final(self):
        nota_final = (self.nota1 + self.nota2 + self.nota3) /3
        print('Nota final:', nota_final)
        if nota_final >= 4.8:
            return 'Aprobado'
        else:
            return 'No superado'
            
laura = Alumno(1234567890, 'Laura Martínez', 4.5,6.7,8.9)


laura.dame_info()
print(laura.nota_final())
        
