import random
random.seed(20220512)

mul_3 =0
mul_5 =0
no_multiplo = 0
mayor = 1
can_pares_mul_11= 0
suma_par_mul_11 =0
for i in range(25000):
    x = random.randint(1,45000)
    #1
    if x % 3 == 0:
        mul_3 +=1
    elif x % 5 ==0:
        mul_5 +=1
    else:
       no_multiplo +=1
    #2
    if int(str(x)[0]) == 1:

        if x > mayor:
            mayor = x
    if x % 2 == 0 and x % 11 == 0 :
        can_pares_mul_11 +=1
        suma_par_mul_11 +=x

promedio = (suma_par_mul_11//can_pares_mul_11)
porcentaje_mul3 = (mul_3 *100) //25000
porcentaje_mul5 = (mul_5 *100) //25000
porcentaje_nomul = (no_multiplo *100) //25000
print("multiplo de 3: ",mul_3)
print("Multiplo de 5 y no de 3: ",mul_5)
print("No son multiplos de 3 ni de 5: ",no_multiplo)
print("El mayor que empieza con 1 es :",mayor)
print("promedio truncado de pares multiplos de 11: ",promedio)
print("porcentaje truncado de multiplos de 3:",porcentaje_mul3)
print("porcentaje truncado de multiplos de 5 y no de 3:",porcentaje_mul5)
print("porcentaje truncado de no multiplos de 3 ni de 5:",porcentaje_nomul)
