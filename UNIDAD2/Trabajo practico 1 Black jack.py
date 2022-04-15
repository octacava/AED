
import random
#Generador aleatoreo de cartas numeros y palo
#cartas_numero =  11,
cartas_numero = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
cartas_palo = "corazones", "pircas", "trebol", "rombo",
ass = 1

carta_1 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_2 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_3 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_4 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_5 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_6 = random.choice(cartas_numero), "de", random.choice(cartas_palo)

# generador de mano croupier

mano_croupier = carta_1 , carta_2,
puntaje_croupier = carta_1[0] + carta_2[0]

# analisis mano croupier
print("El Croupier obtiene dos cartas: " , mano_croupier)
print("Sumando: " , puntaje_croupier , "puntos.")

if carta_1[0] == 11 and carta_2[0] == 11 :
    carta_1 = ass , carta_1[1], carta_1[2]
    mano_croupier = carta_1, carta_2
    puntaje_croupier = carta_1[0] + carta_2[0]
    print("El croupier remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_croupier , "puntos.")

if puntaje_croupier <= 16:
       mano_croupier = carta_1, carta_2, carta_3,
       puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
       print("El croupier obtiene la tercer carta, que es:" , carta_3)
       print("Sumando: " , puntaje_croupier, "puntos.")


if puntaje_croupier > 21 :
      if carta_1[0] == 11:
         carta_1 = ass , carta_1[1], carta_1[2]
         mano_croupier = carta_1, carta_2, carta_3,
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El croupier remplaza el valor 11 por el 1 de su As")
      elif carta_2[0] == 11:
         carta_2 = ass ,  carta_2[1], carta_2[2]
         mano_croupier = carta_1, carta_2, carta_3,
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El croupier remplaza el valor 11 por el 1 de su As")
      elif carta_3[0] == 11:
         carta_3 = ass, carta_3[1], carta_3[2]
         mano_croupier = carta_1, carta_2, carta_3,
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El croupier remplaza el valor 11 por el 1 de su As")



print("Las cartas finales del Croupier son: " , mano_croupier)
print("Sumando: " ,puntaje_croupier , "puntos.")


#generador mano jugador




mano_jugador = carta_4, carta_5
puntaje_jugador = carta_4[0] + carta_5[0]

print("El Jugador recibe dos cartas: " , mano_jugador)
print("Sumando: " , puntaje_jugador , "puntos.")

if carta_4[0] == 11 and carta_5[0] == 11 :
    carta_4 = ass , carta_4[1], carta_4[2]
    mano_jugador = carta_4, carta_5
    puntaje_jugador = carta_4[0] + carta_5[0]
    print("El Jugador remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_jugador , "puntos.")

if puntaje_jugador <= 15:
       mano_jugador = carta_4, carta_5, carta_6
       puntaje_jugador = carta_4[0] + carta_5[0] + carta_6[0]
       print("El Jugador recibe la tercer carta, que es:" , carta_6)
       print("Sumando: " , puntaje_jugador, "puntos.")


if puntaje_jugador > 21 :
      if carta_4[0] == 11:
         carta_4 = ass, carta_4[1], carta_4[2]
         mano_jugador = carta_4, carta_5, carta_6
         puntaje_jugador = carta_4[0] + carta_5[0] + carta_6[0]
         print("El Jugador remplaza el valor 11 por el 1 de su As")
      elif carta_5[0] == 11:
         carta_5 = ass , carta_5[1], carta_5[2]
         mano_jugador = carta_4, carta_5, carta_6
         puntaje_jugador = carta_4[0] + carta_5[0] + carta_6[0]
         print("El Jugador remplaza el valor 11 por el 1 de su As")
      elif carta_6[0] == 11:
         carta_6 = ass , carta_6[1], carta_6[2]
         mano_jugador = carta_4, carta_5, carta_6
         puntaje_jugador = carta_4[0] + carta_5[0] + carta_6[0]
         print("El Jugador remplaza el valor 11 por el 1 de su As")



print("Las cartas finales del Jugador son: " , mano_jugador)
print("Sumando: " ,puntaje_jugador , "puntos.")


if puntaje_croupier > puntaje_jugador:
    print("El Croupier gana la partida. \n Con" , puntaje_croupier , "puntos, contra" , puntaje_jugador, "puntos.")
if puntaje_croupier < puntaje_jugador:
    print("El Jugador gana la partida. \n Con" , puntaje_jugador , "puntos, contra" , puntaje_croupier, "puntos.")


