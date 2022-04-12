segundos = int(input("ingrese los segundos: "))
hora = divmod(segundos, 3600)
min = int(hora[1] // 60)
seg = hora[1] % 60
print("horas: " ,hora[0])
print("minutos: " , min)
print("segundos: " , seg)



