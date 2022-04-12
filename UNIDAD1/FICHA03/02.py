# 2. Fecha como cadena
'''Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa
 una fecha en formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año.
  Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.'''

fecha_inicial = input("Ingrese fecha en formato dd/mm/aaaa: ")

dia = fecha_inicial[0]+fecha_inicial[1]
mes = fecha_inicial[3]+fecha_inicial[4]
año = fecha_inicial[6]+fecha_inicial[7]+fecha_inicial[8]+fecha_inicial[9]
print(f"Día: {dia} - Mes: {mes} - Año: {año}.")

