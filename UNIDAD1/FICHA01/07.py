# Precio del boleto

origen = input("Origen del viaje: ")
destino = input("Destino del viaje: ")
base = float(input("Precio del boleto base: "))
km = float(input("Cantidad de Km: "))
adicional_km = 0.3
precio_boleto = base + km * adicional_km
ahora_12 = round(precio_boleto / 12 ,2)
print(f"El precio del boleto con origen: {origen} y destino: {destino}, es de ${precio_boleto}\n El cual se puede abonar con Ahora 12 en 12 cuotas iguales de ${ahora_12}")

