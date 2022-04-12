# Descuento en medicinas
# Entrada
precio_actual = float(input("Ingrese el precio del medicamento: "))

#proceso
descuento =  precio_actual * 0.35

precio_con_descuento = precio_actual - descuento

# Salida
print(f"El precio actual del medicamento es ${precio_actual}\n El descuento del %35 es: {descuento}\n El precio final del medicamento es ${precio_con_descuento}")

