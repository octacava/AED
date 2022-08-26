
########################################################################################################################
# definicion del registro

#definicion del tipo proyecto
class Proyecto:
   #funcion para asignar los valores a los campoc
   def __init__(self,numero,titulo,fecha,lenguaje,cant_lineas):
     self.numero     = numero
     self.titulo     = titulo
     self.fecha      = fecha
     self.lenguaje   =lenguaje
     self.cant_lineas = cant_lineas

   #funcion de retorno str con datos de los campos
   def __str__(self):
      res=  "Numero: " + str(self.numero) + ", titulo: " + str(self.titulo) + " fecha: " + str(self.fecha) + \
            " lenguaje: " + str(self.lenguaje) + " cantidad de lineas: " + str(self.cant_lineas)
      return res

########################################################################################################################




