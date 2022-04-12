#Polinomio de segundo grado
'''Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
 y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
  Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula
  para el cálculo de las raíces de la ecuación.'''


a = float(input("Ingrese el valor de 'a': "))
b = float(input("Ingrese el valor de 'b': "))
c = float(input("Ingrese el valor de 'c': "))
x = float(input("Ingrese el valor de 'x': "))

polinomio_segundo_grado = (a*x)**2 + b*x + c
discriminante = b ** 2 - 4 * a * c

print(f"El valor del polinomio en el valor x={x} es: {polinomio_segundo_grado}")
print(f'El discriminante del polinomio es: {discriminante}')
