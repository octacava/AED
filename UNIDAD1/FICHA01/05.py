# Conversión de medidas
# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas, pulgadas,  centímetros
# metros
pie = int(input("Ingrese la medida en pies, que desee convertir:\n"))
yarda = pie / 3
pulgada = pie * 12
centimetro = pulgada * 2.54
metro = centimetro / 100

print(f"Conversion de medidad:\n {pie} Pies son equivalentes a:\n {pie} pies = {yarda} Yardas\n {pie} pies = {pulgada} Pulgadas\n {pie} pies = {centimetro} Centimetros\n {pie} pies = {metro} Metros")
