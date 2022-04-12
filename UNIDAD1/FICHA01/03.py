# Área de un triángulo

# Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base,
# #pero sabiendo que su altura es igual al cuadrado de la base. (Observar que la altura no es un dato...
# sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).

base = float(input("Enter the value of the base of the triangle: \n" ))
altura = base**2
area = (base * altura)/ 2

print(f"The area of the triangle is: {area}")

