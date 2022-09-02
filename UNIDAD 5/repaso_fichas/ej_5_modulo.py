'''
Por cada alumno se tienen los siguientes datos: DNI del alumno, el nombre del alumno,
 el apellido del alumno, DNI del Tutor (adulto responsable del niño), el importe de la cuota y el nivel en el que
 cursa el niño (un valor entre 0 y 12 incluidos, de la forma 0: Inicial, 1: Primer Junior, 2: Primer Younger, etc.).
  Se desea almacenar la información referida a los n alumnos en un arreglo de registros de tipo Alumno
   (definir el tipo Alumno y cargar n por teclado).

'''

#definir clase

class Alumno():
    #funcion constructora
    def __init__(self,dni_alumno,nom_alumno,apellido_alumno,dni_tutor,cuota,nivel_curso):


        self.dni_alumno = dni_alumno
        self.nom_alumno = nom_alumno
        self.apellido_alumno = apellido_alumno
        self.dni_tutor = dni_tutor
        self.cuota = cuota
        self.nivel_curso = nivel_curso

    #funcion de salida

    def __str__(self):


        res= 'Dni alumno: ' + str(self.dni_alumno) + ' Nombre alumno: ' + str(self.nom_alumno)  + \
             ' Apellido alumno: '+ str(self.apellido_alumno) + ' Dni tutor: ' + str(self.dni_tutor) + ' Cuota: '+ str(self.cuota) + \
             ' Nivel de curso: ' + str(self.nivel_curso)

        return res
