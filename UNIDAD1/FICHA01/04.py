#  Últimos dígitos
numero = int(input('Ingrese un numero: '))
unidad = numero % 10
decena = numero % 100

print(f"El ultimo digito del numero {numero} es {unidad} \nLos dos ultimos digitos del numero {numero} son {decena}")

