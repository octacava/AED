'''

Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta se registran los
siguientes datos: el número de factura, importe de la factura, el tipo de factura (A, B, C o E), el apellido de la
persona que realiza la compra, y el tipo del perfume vendido (un número entero para indicar su marca, entre 1 y 17,
por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.). Se desea almacenar la información referida a las ventas que realiza la
 perfumería en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de n ventas realizadas. Valide que el importe de la factura sea mayor a 0
y menor a 200000. Valide que el tipo de factura sea alguno de los tipos válidos: A, B, C o E, y valide también que el
tipo de perfume sea un número entero entre 1 y 17 ambos incluidos. Puede hacer la carga en forma manual, o puede generar
los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos
 una debe programar.

2- Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea distinto
de t (x y t son valores que se cargan por teclado). El listado debe salir ordenado de mayor a menor según los apellidos
de las personas que realizaron la compra.

3- Determinar y mostrar el importe total facturado para cada uno de los 17 tipos posibles pero informe por pantalla
solamente el total facturado correspondiente al tipo de perfume z (cargar el número z por teclado).

4- Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de perfume se
encuentre entre 5 y 12 y que no sean con factura de tipo C. Si no existe ninguna venta que cumpla con ese criterio
informarlo por pantalla.

5- Determinar si existe una venta cuyo número de factura sea igual a n (cargar n por teclado) y cuyo importe de
factura sea menor a a un valor p que se carga por teclado. Si existe, mostrar
'''

#import
import random
from modulo import Venta

#funciones______________________________________________________________________________________________________________

def  mostrar_menu():
    print('\n1-Cargar ventas')
    print('2-Mostrar ventas mayores a x, con facturas distintas de T.')
    print('3-Importe total facturado por perfume "x"')
    print('4-Ventas entre cat 5 y 12 con factura no C')
    print('5-Buscar factura "x" y monto menor a "M"')
    print('6-Salir\n')




def cargar_ventas(n, ventas):
    apellidos = ('Garcia','Perez','Lorca','Sanches','Diaz')
    num = len(ventas)
    for i in range(n):
        num += 1
        importe_factura = random.randint(1,199999)
        while importe_factura <1 or importe_factura >= 200000:
            int(input('\nIngrese un importe entre $1 y $200.000: '))
        apellido = random.choice(apellidos).lower()
        tipo_factura = random.choice(('A','B','C','E')).upper()
        while tipo_factura != 'A' and tipo_factura != 'B' and tipo_factura != 'C' and tipo_factura != 'E'and tipo_factura != 'a' and tipo_factura != 'b' and tipo_factura != 'c' and tipo_factura != 'e' :
            tipo_factura = input('\nIngrese el tipo de factura: ').upper()
        tipo_perfume = random.randint(1,17)
        while tipo_perfume <1 or tipo_perfume >17:
             tipo_perfume =int(input('\nIngrese tipo de perfume: '))
     #referenciar objeto
        venta = Venta(num,importe_factura,tipo_factura,apellido,tipo_perfume)

    #almacenar
        ventas.append(venta)



def validar_n():
    n=int(input('\nNumero de ventas a cargar: '))
    while n < 1:
        n = int(input('\nIngrese una cantidad mayor a "0" de ventas '))
    return n


def mostrar_ventas(ventas):
    for i in ventas:
       print(Venta.__str__(i))


def mostrar_ventas_mayores(ventas,x_importe,t_factura_distinta):
    ventas_mayores_distintas = []
    for i in range(len(ventas)):
        if x_importe < ventas[i].importe_factura and t_factura_distinta != ventas[i].tipo_factura :
            ventas_mayores_distintas.append(ventas[i])

           # print(ventas[i].__str__())
        #ordenar de mayor a menor por apellido
        #cantidad de ventas
        n = len(ventas_mayores_distintas)
        #pivot del oredenador
        for j in range(0,n-1):
            #elemento de comparacion
           for t in range(j+1,n):
               #comparar los ordenes para ver si hay que intercambiar
               if ventas_mayores_distintas[j].apellido < ventas_mayores_distintas[t].apellido:
                   ventas_mayores_distintas[j],ventas_mayores_distintas[t] = ventas_mayores_distintas[t],ventas_mayores_distintas[j]
    for p in range(len(ventas_mayores_distintas)):
       print(ventas_mayores_distintas[p].__str__())


def mostrar_total_facturado(ventas, perfume):

        #sumatoria por codigo de perfume
        for i in range(1,18):
            ventas_acumuladas = 0
            #buscar en cada venta

            for elemento in ventas:
               if elemento.tipo_perfume == i:
                ventas_acumuladas += elemento.importe_factura
                #print(ventas_acumuladas)
            if i == perfume:

              print('\nEl importe acumulado para la categoria de perfume '+str(i)+' es: $'+str(ventas_acumuladas))


def mostrar_ventas_entre5y12_noc(ventas):
    for cliente in ventas:
        if (cliente.tipo_perfume >4 and cliente.tipo_perfume <13 ) and cliente.tipo_factura != "C":
            print(f'\nNumero de factura: {cliente.num}  Apellido del cliente: {cliente.apellido} Importe de la compra: {cliente.importe_factura}')
        else: print('\nNo se encontraron coincidencias.')

def buscar_factura_menora(ventas,x_factura,m_importe):
    for buscada in ventas:
        if buscada.num == x_factura and buscada.importe_factura < m_importe:
            print(buscada)
        else: print('\nNo se encontraron coincidencias.')


def principal():
    # vectores
    ventas= [ ]
    ## menu
    op=-1
    while op != 6:
        mostrar_menu()
        op = int(input('\nIngrese una opcion: '))
        #analizar opciones
        if op == 1:
            n = validar_n()
            cargar_ventas(n,ventas)
            #mostrar_ventas(ventas)
            
        elif op == 2:
            x_importe =int(input('\nIngrese el importe de ventas a buscar: '))
            t_factura_distinta =input('\nIngrese el tipo de factura que no debe seleccionar: ').upper()
            mostrar_ventas_mayores(ventas,x_importe,t_factura_distinta)


        elif op == 3:
            perfume = int(input("\nIngrese el codigo de perfume a consultar: "))
            mostrar_total_facturado(ventas,perfume)

        elif op == 4:
            mostrar_ventas_entre5y12_noc(ventas)
        elif op == 5:
            x_factura = int(input('\nIngrese numero de factura que desea buscar: '))
            m_importe = int(input('\nIngrese el monto al cual las ventas deben ser menor: '))
            buscar_factura_menora(ventas,x_factura,m_importe)
        elif op == 6:
            print('\nProceso finalizado.')



### main
if __name__ == '__main__':
    principal()


