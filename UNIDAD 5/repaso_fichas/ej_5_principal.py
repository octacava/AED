'''
5. (Parcial 2020) La Academia de Ingles
Una academia de inglés para niños de escolaridad primaria y nivel inicial, desea un programa para procesar los datos de
 sus alumnos. Por cada alumno se tienen los siguientes datos: DNI del alumno, el nombre del alumno,
 el apellido del alumno, DNI del Tutor (adulto responsable del niño), el importe de la cuota y el nivel en el que
 cursa el niño (un valor entre 0 y 12 incluidos, de la forma 0: Inicial, 1: Primer Junior, 2: Primer Younger, etc.).
  Se desea almacenar la información referida a los n alumnos en un arreglo de registros de tipo Alumno
   (definir el tipo Alumno y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes
tareas:

1- Cargar el arreglo pedido con los datos de los n alumnos. Valide que el número de nivel sea un valor entre 0 y 12
(ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática
(con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de todos los alumnos, en un listado ordenado de menor a mayor según el apellido del alumno.

3- Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel
 (o sea, 13 contadores). Muestre sólo los resultados diferentes de 0.

4- Determinar el monto total que debe abonar el Tutor con número de DNI igual a x, siendo x un valor que se carga por
teclado (sumar los importes de las cuotas de los niños que el Tutor tiene a su cargo).

5- Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
 Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
 Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda,
  debe mostrar sólo el primero que encuentre.
'''

#import

import random
from ej_5_modulo import Alumno


# Funciones



def mostrar_menu():

       print('\n1-Cargar cantidad de alumnos. ')
       print('2-Mostrar alumnos ordenados M a Men por apellido.')
       print('3-Cantidad de alumnos por nivel. ')
       print('4-Monto a abonar por el tutor. ')
       print('5-Buscar alumno y otorgar 10% de descuento.')
       print('6-Salir.\n')


def cargar_alumnos( n_alumnos,alumnos):

    #generar datos en funcion de n

   #dni_alumno,nom_alumno,apellido_alumno,dni_tutor,cuota,nivel_curso

   for i in range(0,n_alumnos):
        dni_alumno = random.randint(40000000,55000000)
        nom_alumno =random.choice (('Juan','Ana','Lucas','Marcela','Carlos')).lower()
        apellido_alumno = random.choice(('Garcia','Perez','Lorca','Sanches','Diaz')).lower()
        dni_tutor = random.randint(10000000,35000000)
        cuota= random.randint(6000,15000)
        nivel_curso = random.randint(0,12)
        if nivel_curso <0 or nivel_curso >12:
            int(input('\nIngrese un curso entre 0 y 12: '))

        #crear el registro

        alumno = Alumno(dni_alumno,nom_alumno,apellido_alumno,dni_tutor,cuota,nivel_curso)

        #grabarlo en el vector
        alumnos.append(alumno)


def mostrar_alumnos(alumnos):
    for persona in alumnos:
        print(persona)


def ordenar_alumnos(alumnos):

    n=len(alumnos)
    for pivot in range(n-1):
        for sig in range(pivot+1,n):
          if alumnos[pivot].apellido_alumno < alumnos[sig].apellido_alumno:
              alumnos[pivot] ,alumnos[sig] = alumnos[sig],alumnos[pivot]
    mostrar_alumnos(alumnos)


def cantida_por_nivel(alumnos):
    for nivel in range(0,13):
        cantidad_alumnos_nivel=0
        for alumno in alumnos:
            if alumno.nivel_curso == nivel:
                cantidad_alumnos_nivel +=1
        if cantidad_alumnos_nivel != 0:
                print(f'Nivel {nivel} = {cantidad_alumnos_nivel} alumnos')


def monto_abonar(alumnos,dni_t):
    monto_cuota= 0
    cantidad_cuotas = 0
    for tutor in range(len(alumnos)):

        if alumnos[tutor].dni_tutor == dni_t:
            monto_cuota += alumnos[tutor].cuota
            cantidad_cuotas +=1

    if monto_cuota != 0:
             print('El tutor '+str(dni_t) + ' debe abonar '+str(cantidad_cuotas) + ' cuotas, por un importe de: $'+str(monto_cuota))
    monto_cuota= 0
    cantidad_cuotas = 0


def otorgar_descuento(alumnos, buscar_alumno):
    no_hay =True
    for al in range(len(alumnos)):

        if alumnos[al].apellido_alumno == buscar_alumno:
            alumnos[al].cuota = round(alumnos[al].cuota * .9,2)
            print(alumnos[al])
            no_hay= False
    if no_hay :
            print('\nNo se encontro alumno con el apellido: '+ buscar_alumno)
def principal():

   #vectores
    alumnos = []

   #menu de opciones
    op = -1

    while op != 6:
       mostrar_menu()
       op = int(input('\nIngrese la opcion: '))


       if op == 1:
           n_alumnos = int(input('\nNumero de alunmos: '))
           cargar_alumnos(n_alumnos, alumnos)
           #mostrar_alumnos(alumnos)
       elif op == 2:
           ordenar_alumnos(alumnos)
       elif op == 3:
           cantida_por_nivel(alumnos)

       elif op == 4:
           dni_t = int(input('\nIngrese DNI de tutor: '))
           monto_abonar(alumnos,dni_t)

       elif op == 5:
           buscar_alumno = input('\nIngrese apellido de alumno: ').lower()
           otorgar_descuento(alumnos,buscar_alumno)

       elif op == 6:

           print('\nProceso finalizado.')



# ejecutar principal

if __name__ == '__main__':
    principal()
