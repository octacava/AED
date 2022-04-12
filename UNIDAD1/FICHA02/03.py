#3. Ecuación de Einstein
#La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
#E = mc2
#Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg. #
# Desarrolle un programa que lea el valor una masa m en kilogramos #
# y obtenga la cantidad de energía E producida en la conversión.


print('Calculo de conversion de masa en energia (Einstein)')
m = float(input("Ingrese la masa expresada en kg : "))
C = 299792.458
e = m * (C**2)

print(F"La energia de la masa ingresada es: {e}")
