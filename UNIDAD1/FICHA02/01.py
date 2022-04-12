#Cuadrados y cubos
#Leer dos números y calcular:La suma de sus cuadrados. El promedio de sus cubos.

a = float(input("ingrese un numero: "))
b = float(input("ingrese un numero: "))

suma_cuadrados = a**2 + b**2
promedio_de_cubos = (a**3 + b**3) /2

print(f"La suma de sus cuadrados es : {suma_cuadrados}\nEl promedio de sus cubos es: {promedio_de_cubos}")
