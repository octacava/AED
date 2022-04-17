
import random
#Generador aleatoreo de cartas numeros y palo

cartas_numero ="As", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K",
cartas_palo = "corazones", "pircas", "trebol", "rombo",



#contador de figuras
figura = 0

#asignacion de cartas, carta_1 carta_2 y ocacionalmente carta_3 asignadas al crupier.
carta_1 = random.choice(cartas_numero),  random.choice(cartas_palo)
carta_2 = random.choice(cartas_numero),  random.choice(cartas_palo)
carta_3 = random.choice(cartas_numero),  random.choice(cartas_palo)

#asignacion de cartas, carta_4 carta_5 y ocacionalmente carta_6 asignadas al jugador.
carta_4 = random.choice(cartas_numero),  random.choice(cartas_palo)
carta_5 = random.choice(cartas_numero),  random.choice(cartas_palo)
carta_6 = random.choice(cartas_numero),  random.choice(cartas_palo)

# generador de mano crupier. Asignamos las dos primeras cartas y verificamos si alguna es una figura

mano_crupier = carta_1 , carta_2,
if carta_1[0] == "J" or carta_1[0] == "Q" or carta_1[0] == "K" or carta_2[0] == "J" or carta_2[0] == "Q" or carta_2[0] == "K" :
    figura += 1


puntaje_crupier = 0
if carta_1[0] == "As":
    puntaje_crupier = 11
elif carta_1[0] == "J" or carta_1[0] == "Q" or carta_1[0] == "K":
    puntaje_crupier = 10
else:
    puntaje_crupier = carta_1[0]

if carta_2[0] == "As":
    puntaje_crupier += 11
elif carta_2[0] == "J" or carta_2[0] == "Q" or carta_2[0] == "K":
    puntaje_crupier += 10
else:
    puntaje_crupier += carta_2[0]




# analisis mano crupier
print("El Crupier obtiene dos cartas: \n", carta_1[0], "de", carta_1[1], "\n", carta_2[0], "de", carta_2[1] )
print("Sumando: " , puntaje_crupier , "puntos.")

#se verifica si las 2 cartas  son As. En caso de que las dos sean as (suman 22)se remplaza el valor de la primera por 1
if carta_1[0] == "As" and carta_2[0] == "As" :
    puntaje_crupier -= 10
    print("El crupier remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_crupier , "puntos.")
imprimir_carta3 = 0
#verificamos si el puntaje es 16 o menos, y en ese caso repartimos la tercer carta
if puntaje_crupier <= 16:
       mano_crupier = carta_1, carta_2, carta_3,
       imprimir_carta3 += 1
       if carta_3[0] == "J" or carta_3[0] == "Q" or carta_3[0] == "K":
          figura += 1
       if carta_3[0] == "As":
          puntaje_crupier += 11
       elif carta_3[0] == "J" or carta_3[0] == "Q" or carta_3[0] == "K":
          puntaje_crupier += 10
       else:
          puntaje_crupier += carta_3[0]

       print("El crupier obtiene la tercer carta, que es:\n", carta_3[0], "de", carta_3[1])
       print("Sumando: " , puntaje_crupier, "puntos.")


#comprobamos si el puntaje es mayor a 21, y si alguna carta es el as. Remplazamos por el valor 1 y volvemos a sumar.
if puntaje_crupier > 21:
      if carta_3[0] == "As":
         puntaje_crupier -= 10
         print("El crupier remplaza el valor 11 por el 1 de su As")
      elif not(carta_1[0] == carta_2[0] and carta_1[0] == "As"):
         if carta_1[0] == "As":
            puntaje_crupier -= 10
            print("El crupier remplaza el valor 11 por el 1 de su As")
         elif carta_2[0] == "As":
            puntaje_crupier -= 10
            print("El crupier remplaza el valor 11 por el 1 de su As")


# cartas finales crupier carta_1 carta_2 y dependiendo el puntaje carta_3
print("El Crupier termina la mano con las siguientes cartas:\n",carta_1[0], "de",carta_1[1],"\n",carta_2[0],"de", carta_2[1] )
if imprimir_carta3 ==1 :
    print(  carta_3[0],"de", carta_3[1])
print("Sumando: " ,puntaje_crupier , "puntos.")


#generador mano jugador


# generador de mano jugador. Asignamos las dos primeras cartas y verificamos si alguna es una figura

mano_jugador = carta_4, carta_5
if carta_4[0] == "J" or carta_4[0] == "Q" or carta_4[0] == "K" or  carta_5[0] == "J" or carta_5[0] == "Q" or carta_5[0] == "K":
   figura += 1
puntaje_jugador  = 0
if carta_4[0] == "As":
    puntaje_jugador = 11
elif carta_4[0] == "J" or carta_4[0] == "Q" or carta_4[0] == "K":
    puntaje_jugador = 10
else:
    puntaje_jugador = carta_4[0]

if carta_5[0] == "As":
    puntaje_jugador += 11
elif carta_5[0] == "J" or carta_5[0] == "Q" or carta_5[0] == "K":
    puntaje_jugador += 10
else:
    puntaje_jugador += carta_5[0]

print("El Jugador recibe dos cartas: \n", carta_4[0], "de", carta_4[1], "\n", carta_5[0], "de", carta_5[1] )
print("Sumando: " , puntaje_jugador , "puntos.")

#se verifica si las 2 cartas  son As. En caso de que las dos sean as (suman 22)se remplaza el valor de la primera por 1

if carta_4[0] == "As" and carta_5[0] == "As" :
    puntaje_jugador -= 10
    print("El Jugador remplaza el valor 11 por el 1 de su As")
    print("Sumando ahora:" , puntaje_jugador , "puntos.")

imprimir_carta6 = 0
#verificamos si el puntaje es 15 o menos, y en ese caso repartimos la tercer carta
if puntaje_jugador <= 15:
       mano_jugador = carta_4, carta_5, carta_6,
       if carta_6[0] == "J" or carta_6[0] == "Q" or carta_6[0] == "K":
           figura += 1
       imprimir_carta6 += 1
       if carta_6[0] == "As":
          puntaje_jugador += 11
       elif carta_6[0] == "J" or carta_6[0] == "Q" or carta_6[0] == "K":
          puntaje_jugador += 10
       else:
          puntaje_jugador += carta_6[0]

       print("El Jugador recibe la tercer carta, que es:\n", carta_6[0], "de", carta_6[1])
       print("Sumando: " , puntaje_jugador, "puntos.")


#comprobamos si el puntaje es mayor a 21, y si alguna carta es el as. Remplazamos por el valor 1 y volvemos a sumar.
if puntaje_jugador > 21:
      if carta_6[0] == "As":
         puntaje_jugador -= 10
         print("El Jugador remplaza el valor 11 por el 1 de su As")
      elif not(carta_4[0] == carta_5[0] and carta_4[0] == "As"):
         if carta_4[0] == "As":
            puntaje_jugador -= 10
            print("El Jugador remplaza el valor 11 por el 1 de su As")
         elif carta_5[0] == "As":
            puntaje_jugador -= 10
            print("El Jugador remplaza el valor 11 por el 1 de su As")


# cartas finales jugador carta_4 carta_5 y dependiendo el puntaje carta_6

print("El Jugador termina la mano con las siguientes cartas:\n",carta_4[0], "de",carta_4[1],"\n",carta_5[0],"de", carta_5[1] )
if imprimir_carta6 ==1 :
    print(  carta_6[0],"de", carta_6[1])
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

if carta_1[1] == carta_4[1] :
    print("La primer carta del jugador es del mismo palo que la primer carta del crupier : " , carta_4[1])
    if carta_1[0] == carta_4[0] :
        print("Tambien ambas primeras cartas son del mismo numero: " , carta_4[0])


if figura :
   print("Salio al menos una figura durante la partida.", figura, "En total")

