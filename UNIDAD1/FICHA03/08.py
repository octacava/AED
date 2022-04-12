#8. Calculo Distancia de Viaje

DT = 3641.3 *1000
x = float(input("ingrese la distancia recorrida en m :"))
distancia_recorrida = divmod(x,1000)
porcentaje_recorrido = (x / DT) * 100

print(f"recorrio {distancia_recorrida[0]} km y {distancia_recorrida[1] } metros")
print(f" Que representa el {round(porcentaje_recorrido, 2 ) }% del recorrido")
