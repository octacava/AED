

# Funcion de ejecucion

#Calculamos lacantidad de palabras que contiene el texto


def cant_pal(oracion):
      palabras = 0
      for i in oracion:
        if i == " " or i == ".":
            palabras+= 1

      return palabras


# Cantidad de palabras con 2 o mas digitos y k o r


def k_r_2(oracion):

    digitos= 0
    k_o_r = False
    cant_palabras_k_r_digitos = 0

    for i in oracion:
         if i != " " and i != ".":
             if i in '0123456789':
                 digitos +=1
             if i == "k" or i == "K" or i == "r" or i == "R":
                 k_o_r =True





         else:
             if digitos >= 2 and k_o_r == True:
                 cant_palabras_k_r_digitos += 1
                 digitos = 0
                 k_o_r = False

    return cant_palabras_k_r_digitos

#Calculamos porcentaje de palabras con mas vocales


def mas_consonantes(palabrastot, oracion):
  palabra_actual = ""
  cantidad_palabras_mas_cons = 0
  vocales = ""
  for i in oracion:
       if i != " " and i != "." :
          palabra_actual += i
          if i in "aeiouAEIOUáéíóúÁÉÍÓÚ" :
                 vocales +=i

       else:
           tamano_palabra =len(palabra_actual)
           cantidad_vocales = len(vocales)


           palabra_actual = ""


           vocales =""

           if (tamano_palabra - cantidad_vocales) > cantidad_vocales:
               cantidad_palabras_mas_cons +=1


  porcentaje_palabras_consonantes = round((cantidad_palabras_mas_cons*100)/palabrastot,2)
  return porcentaje_palabras_consonantes


#Calculamos cuantas palabres tienen entre sus primeras tres posiciones el mismo caracter que la primera palabra

def igual_que_primera(oracion):
    primer_caracter = oracion[0].lower()
    repe= 1

    posicion = 0

    for i in oracion:
          posicion += 1

          if i == " ":
              if (oracion[posicion].lower() ==primer_caracter) or (oracion[posicion+1].lower() ==primer_caracter) or (oracion[posicion+2].lower() ==primer_caracter):

                  repe += 1



    return repe

# buscamos palabras con la exprecion se, pero que no empiece con la exprecion se


def no_empiece_se(oracion):

     contiene_se = 0
     anterior= " "
     posicion = 0

     for i in oracion:
         posicion +=1
         if anterior != " ":
             if (oracion[posicion-1] == "s" or oracion[posicion-1]=="S") and ( oracion[posicion]=="E" or oracion[posicion]=="e"):
                 contiene_se += 1

         anterior = i
     return contiene_se

def adornos_print():
    print("\n ","#" *100, "\n")

def test():
    #Datos
    adornos_print()
    texto = input('\tIngrese un texto, separando\n      las palabras con un espacio y finalizando\n \t\tla oracion con un punto:')


    #funciones
    cantidad_palabras = cant_pal(texto)
    palabras_2dig_kor = k_r_2(texto)
    porcentaje_mas_consonantes = mas_consonantes(cantidad_palabras,texto)
    primera_letra_primeras_3 = igual_que_primera(texto)
    cant_se_pero_no_empiece_se = no_empiece_se(texto)


    #impreciones
    adornos_print()

    #punto 1
    print("La cantidad de palabras que contienen 2 digitos o mas y la letra k o r son : ", palabras_2dig_kor)
    adornos_print()

    #punto 2
    print("El porcentaje de palabras que contiene mas consonantes que vocales es: %",porcentaje_mas_consonantes)
    adornos_print()

    #punto 3
    print("La cantidad de palabras que contiene dentro de sus primeras tres pociciones el mismo caracter\n\t\t que la primer letra de la oracion son:", primera_letra_primeras_3)
    adornos_print()

    #punto 4
    print("La cantidad de palabras que contienen la exprecion 'se' pero no comienza con 'se' son :", cant_se_pero_no_empiece_se)
    adornos_print()


#script principal

if __name__ == "__main__":
    test()
