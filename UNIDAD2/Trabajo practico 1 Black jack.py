
import random
#Generador aleatoreo de cartas numeros y palo

cartas_numero = 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11,
cartas_palo = "corazones", "pircas", "trebol", "rombo",

# ass valor alternativo del 11
ass = 1

#contador de figuras
figura = 0

#asignacion de cartas, carta_1 carta_2 y ocacionalmente carta_3 asignadas al crupier.
carta_1 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_2 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_3 = random.choice(cartas_numero), "de", random.choice(cartas_palo)

#asignacion de cartas, carta_4 carta_5 y ocacionalmente carta_6 asignadas al jugador.
carta_4 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_5 = random.choice(cartas_numero), "de", random.choice(cartas_palo)
carta_6 = random.choice(cartas_numero), "de", random.choice(cartas_palo)

# generador de mano crupier. Asignamos las dos primeras cartas y verificamos si alguna es una figura

mano_crupier = carta_1 , carta_2,
puntaje_crupier = carta_1[0] + carta_2[0]
if carta_1[0] == 10 or carta_2[0] == 10 :
    figura += 1

# analisis mano crupier
print("El Crupier obtiene dos cartas: " , mano_crupier)
print("Sumando: " , puntaje_crupier , "puntos.")

#se verifica si las 2 cartas  son As. En caso de que las dos sean as (suman 22)se remplaza el valor de la primera por 1
if carta_1[0] == 11 and carta_2[0] == 11 :
    carta_1 = ass , carta_1[1], carta_1[2]
    mano_crupier = carta_1, carta_2
    puntaje_crupier = carta_1[0] + carta_2[0]
    print("El crupier remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_crupier , "puntos.")

#verificamos si el puntaje es 16 o menos, y en ese caso repartimos la tercer carta
if puntaje_crupier <= 16:
       mano_crupier = carta_1, carta_2, carta_3,
       puntaje_crupier = carta_1[0] + carta_2[0] + carta_3[0]
       print("El crupier obtiene la tercer carta, que es:" , carta_3)
       print("Sumando: " , puntaje_crupier, "puntos.")
       if carta_3[0] == 10 :
        figura += 1

#comprobamos si el puntaje es mayor a 21, y si alguna carta es el as. Remplazamos por el valor 1 y volvemos a sumar.
if puntaje_crupier > 21 :
      if carta_1[0] == 11:
         carta_1 = ass , carta_1[1], carta_1[2]
         mano_crupier = carta_1, carta_2, carta_3,
         puntaje_crupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El crupier remplaza el valor 11 por el 1 de su As")
      elif carta_2[0] == 11:
         carta_2 = ass ,  carta_2[1], carta_2[2]
         mano_crupier = carta_1, carta_2, carta_3,
         puntaje_crupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El crupier remplaza el valor 11 por el 1 de su As")
      elif carta_3[0] == 11:
         carta_3 = ass, carta_3[1], carta_3[2]
         mano_crupier = carta_1, carta_2, carta_3,
         puntaje_crupier = carta_1[0] + carta_2[0] + carta_3[0]
         print("El crupier remplaza el valor 11 por el 1 de su As")


# cartas finales crupier carta_1 carta_2 y dependiendo el puntaje carta_3
print("Las cartas finales del Crupier son: " , mano_crupier)
print("Sumando: " ,puntaje_crupier , "puntos.")


#generador mano jugador


# generador de mano jugador. Asignamos las dos primeras cartas y verificamos si alguna es una figura

mano_jugador = carta_4, carta_5
puntaje_jugador = carta_4[0] + carta_5[0]
if carta_4[0] == 10 or carta_5[0] == 10 :
    figura += 1

print("El Jugador recibe dos cartas: " , mano_jugador)
print("Sumando: " , puntaje_jugador , "puntos.")

#se verifica si las 2 cartas  son As. En caso de que las dos sean as (suman 22)se remplaza el valor de la primera por 1
if carta_4[0] == 11 and carta_5[0] == 11 :
    carta_4 = ass , carta_4[1], carta_4[2]
    mano_jugador = carta_4, carta_5
    puntaje_jugador = carta_4[0] + carta_5[0]
    print("El Jugador remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_jugador , "puntos.")

#verificamos si el puntaje es 15 o menos, y en ese caso repartimos la tercer carta
if puntaje_jugador <= 15:
       mano_jugador = carta_4, carta_5, carta_6
       puntaje_jugador = carta_4[0] + carta_5[0] + carta_6[0]
       print("El Jugador recibe la tercer carta, que es:" , carta_6)
       print("Sumando: " , puntaje_jugador, "puntos.")
       if carta_6[0] == 10 :
        figura += 1

#comprobamos si el puntaje es mayor a 21, y si alguna carta es el as. Remplazamos por el valor 1 y volvemos a sumar.
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

# cartas finales jugador carta_4 carta_5 y dependiendo el puntaje carta_6

print("Las cartas finales del Jugador son: " , mano_jugador)
print("Sumando: " ,puntaje_jugador , "puntos.")

#Desarrollo de la mano

#determinar si algun participante se exedio de puntos o ambos

if puntaje_crupier != puntaje_jugador and puntaje_crupier <22 and puntaje_jugador < 22:
    if puntaje_crupier > puntaje_jugador :
        print("El Crupier gana la partida. \n Con" , puntaje_crupier , "puntos, contra" , puntaje_jugador, "puntos.")

    else:
        print("El Jugador gana la partida. \n Con" , puntaje_jugador , "puntos, contra" , puntaje_crupier, "puntos.")

if puntaje_crupier < 22 and puntaje_jugador > 21 :
     print("El Crupier gana la partida. \n Con" , puntaje_crupier , "puntos, El jugador se pasa de 21.")

elif puntaje_jugador < 22 and puntaje_crupier > 21 :
     print("El Jugador gana la partida. \n Con" , puntaje_jugador , "puntos, El crupier se pasa de 21.")
elif  puntaje_jugador >21 and puntaje_crupier > 21 :
     print("Ambos participantes exeden el maximo de puntos.")
elif puntaje_jugador == puntaje_crupier:
     print("Se produjo un Empate")

#comprobamos si la primer carta del jugador, es del mismo palo que la del crupier.
# En caso afirmativo comparamos si tambien son del mismo numero

if carta_1[2] == carta_4[2] :
    print("La primer carta del jugador es del mismo palo que la primer carta del crupier : " , carta_4[2])
    if carta_1[0] == carta_4[0] :
        print("Tambien ambas primeras cartas son del mismo numero: " , carta_4[0])


if figura :
   print("Salio al menos una figura durante la partida.")
