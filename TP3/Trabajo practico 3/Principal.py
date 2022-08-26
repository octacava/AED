'''

Una empresa de desarrollo de software de nuestra ciudad nos encarga un sistema para la gestión de Proyectos de Software.
 De cada proyecto se conoce:
*Número de proyecto
*Título
*Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
*Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
*Cantidad de líneas de código
Se pide desarrollar un programa en dos módulos: uno de ellos debe contener la definición de la clase del regisstro
y las funciones básicas que permitan manejar un registro, y el otro debe contener el programa principal,
que debe estar controlado por un menú de opciones para permitir hacer lo siguiente:

1) Cargar proyectos: La generación de n proyectos de software cargados en un arreglo de registros. Para ello se pueden
generar los datos totalmente aleatorios o bien contar con proyectos completos precargados e ir seleccionando
aleatoriamente entre los mismos. Cada vez que selecciona esta opción durante la ejecución se agregarán datos al arreglo,
 sin eliminar los que ya estaban cargados. El número del proyecto no debe repetirse dentro del arreglo.

2) Listar proyectos: Mostrar todos los proyectos contenidos en el arreglo, pero ordenados alfabéticamente por título.
 Cada proyecto debe ocupar un máximo de dos líneas en pantalla y en lugar de mostrarse el identificador del lenguaje
 se debe mostrar su nombre.

3) Actualizar proyecto: Buscar si existe un proyecto con número x, siendo x un valor que se ingrese por teclado.
Si existe, se debe permitir modificar su cantidad de líneas de código y la fecha de actualización
(recuerde que debe cumplir con el formato dd-mm-yyyy). Si no existe, debe indicar con un mensaje.

4) Resumen por lenguaje: Calcular la cantidad de líneas de código acumuladas por lenguaje. Mostrar los resultados
 teniendo en cuenta que se debe visualizar el nombre del lenguaje en lugar del código.

5) Resumen por año:  Calcular la cantidad de proyectos por año de actualización, considerando los años entre 2000 y 2022
 inlcuidos ambos. Mostrar los resultados sólo de los años que tengan algún proyecto de software.

6) Filtrar lenguaje: Mostrar los proyectos de software ordenados por número de proyecto de manera ascendente,
del lenguaje ln, siendo ln un valor ingresado por teclado.

7) Productividad: A partir del resultado obtenido en el punto 5, determinar el año con mayor cantidad de proyectos
 actualizados, considerando mostrar todos los años si fuera más de uno con dicha cantidad.

'''

#----------------------------------------------------------------------------------------------------------------------
#importar librerias
from modulo_clases import *
import random

#----------------------------------------------------------------------------------------------------------------------
# Definicion de funciones

def mostrar_menu():
    print('| '*22,'\n')
    print('\tMenu:')
    print('1- Cargar proyectos')
    print('2- Listar proyectos')
    print('3- Actualizar proyecto')
    print('4- Resumen por lenguaje')
    print('5- Resumen por año')
    print('6- Filtrar lenguaje')
    print('7- Productividad')
    print('8- Salir del programa')

def validar_n():
    n = 0
    while n <= 0:
      n=int(input('Ingrese el numero de proyectos a gestionar : '))
    return n

# Punto 1_______________________________________________________________________________________________________________
def crear_titulo():
    primer_palabra = ['Medidor','Contador','Seleccionador','Registrador', 'Archibador', 'calculador']
    segunda_palabra= [ 'unidades', 'autos','personal', 'proyectos', ]
    tercer_palabra = ['beta.', '2.0.', 'pro.', '3.0.', 'secret proyect.']
    titulo = random.choice(primer_palabra) +' de '+random.choice(segunda_palabra) + ' '+random.choice(tercer_palabra)
    return  titulo


def crear_fecha():
   dia = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
       '23','24','25','26','27','28','29','30','31']
   mes = ['01','02','03','04','05','06','07','08','09','10','11','12']

   anio = str(random.randint(2000,2022))

   fecha = random.choice(dia)+'/'+ random.choice(mes)+'/'+anio
   return fecha


def crear_lenjuaje():
    lenguaje = ['Python','Java','C++','Javascript','Shell','HTML','Ruby','Swift','C#','VB','Go']
    lenguaje_proyecto = random.choice(lenguaje)
    return lenguaje_proyecto


def crear_cant_lineas():
    lineas=random.randint(1,250)
    return lineas

def crear_proyectos(n,vec,):
    #generar tantos proyectos como n pide
    numero = len(vec)
    for i in range (n):
       numero +=1
       titulo = crear_titulo()
       fecha  = crear_fecha()
       lenguaje = crear_lenjuaje()
       cant_lineas = crear_cant_lineas()


    #referenciar los atributos

       proyecto = Proyecto(numero,titulo,fecha,lenguaje,cant_lineas)

    #almacenar proyectos
       vec.append(proyecto)

#Punto 2 _______________________________________________________________________________________________________________

#Scrip principal
def mostrar_proyecto(vec):
    for i in vec:
        print(Proyecto.__str__(i))


def main():

    vec = []
    #titulo
    print('\n----- Gestor de Proyectos Aed 2022 -----  \n')

    #menu de 8 opciones con verificacion
    op = 0

    while op != 8 :
        mostrar_menu()
        #print('| '*22)
        op=int(input('\nIngrese el numero del menu que quiera acceder: \n'))
        #opcion 1 Cargar proyectos
        if op == 1:
            n=validar_n()
            crear_proyectos(n,vec)

        elif op == 2:
            mostrar_proyecto(vec)
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            print("Sesion finalizada. ")
        else:
            print('\n\tIngrese una opcion valida, por favor.\n')





#----------------------------------------------------------------------------------------------------------------------
#Invocacion scrip principal
if __name__ == '__main__':
    main()
