# Votación en el Congreso
# En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita ingresar
# la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

# Entradas
a_favor = int(input("Votos a favor: "))
en_contra = int(input("Votos en contra: "))

total_votos = a_favor + en_contra

porcentaje_a_favor = (a_favor / total_votos) *100
porcentaje_en_contra = (en_contra / total_votos) * 100

print(f"Votos a favor %{porcentaje_a_favor}\nvotos en contra %{porcentaje_en_contra}")
