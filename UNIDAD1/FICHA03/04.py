#4. Duración de un vuelo
'''Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
 determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto
  al hotel que ha reservado, ¿a qué hora llegara al mismo?'''

import PySimpleGUI as psg

salida = psg.popup_get_text("Hora de salida del vuelo 'hs:min':" , "Aeromatic")
llegada = psg.popup_get_text("Hora de llegada del vuelo 'hs:min':" , "Aeromatic")

hora_llegada = int(llegada[0] + llegada[1])*60
min_llegada = int(llegada[3] + llegada[4])
hora_salida = int(salida[0] + salida[1])*60
min_salida = int(salida[3] + salida[4])

print("El vuelo dura:" , (hora_llegada+min_llegada) - (hora_salida+min_salida) ,"minutos." )
print ("El tiempo total hasta el hotel es de : " , (hora_llegada+min_llegada) - (hora_salida+min_salida) + 45 ,"minutos." )
