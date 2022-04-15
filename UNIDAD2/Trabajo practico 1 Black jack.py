
import random
#Generador aleatoreo de cartas numeros y palo
cartas_numero = 4, 7, 11,
#cartas_numero = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
cartas_palo = "corazones", "pircas", "trebol", "rombo",
ass = 1

carta_1 = random.choice(cartas_numero), random.choice(cartas_palo)
carta_2 = random.choice(cartas_numero), random.choice(cartas_palo)
carta_3 = random.choice(cartas_numero), random.choice(cartas_palo)
carta_4 = random.choice(cartas_numero), random.choice(cartas_palo)
carta_5 = random.choice(cartas_numero), random.choice(cartas_palo)
carta_6 = random.choice(cartas_numero), random.choice(cartas_palo)

# generador de mano croupier

mano_croupier = carta_1, carta_2
puntaje_croupier = carta_1[0] + carta_2[0]

# analisis mano croupier
print("original" , mano_croupier)
print(puntaje_croupier)

if carta_1[0] == 11 and carta_2[0] == 11 :
    carta_1 = ass , carta_1[1]
    mano_croupier = carta_1, carta_2
    puntaje_croupier = carta_1[0] + carta_2[0]

if puntaje_croupier <= 16:
       mano_croupier = carta_1, carta_2, carta_3
       puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
       #print(mano_croupier)
       #print(puntaje_croupier)


if puntaje_croupier > 21 :
      if carta_1[0] == 11:
         carta_1 = ass , carta_1[1]
         mano_croupier = carta_1, carta_2, carta_3
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
      elif carta_2[0] == 11:
         carta_2 = ass , carta_2[1]
         mano_croupier = carta_1, carta_2, carta_3
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]
      elif carta_3[0] == 11:
         carta_3 = ass , carta_3[1]
         mano_croupier = carta_1, carta_2, carta_3
         puntaje_croupier = carta_1[0] + carta_2[0] + carta_3[0]

#print(mano_croupier)
#print(puntaje_croupier)
#print(carta_1[0], carta_2[0], carta_3[0])
#else:
  #print("win")
  #print(mano_croupier)
  #print(puntaje_croupier)

print(mano_croupier)
print(puntaje_croupier)


#generador mano jugador




mano_jugador = carta_4, carta_5
puntaje_jugador = int(carta_4[0])+int(carta_5[0])




#print("jugador: " , mano_jugador)
#print(puntaje_jugador)

