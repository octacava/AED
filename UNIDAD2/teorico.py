dato1 = int(input("hora de salida"))
dato2 = int(input("minuto de salida"))
dato3 = int(input("hora de llegada"))
dato4 = int(input("minuto de llegada"))

if dato3 < dato1:
    horaNegativa = dato3+24
    TotalMinSalida = (dato1*60) + dato2
    TotalMinLlegada = (horaNegativa*60) + dato4

    Calculo = TotalMinLlegada - TotalMinSalida
    RESTOalHotel = Calculo - 45
    CambiarCalculoAHora = RESTOalHotel//60
    CambiarCalculoAMinuto = RESTOalHotel % 60

    print(f"Tarda el Avion un total de {CambiarCalculoAHora} de horas y un total de {CambiarCalculoAMinuto} de minutos")
else:
    TotalMinSalida = (dato1*60) + dato2
    TotalMinLlegada = (dato3*60) + dato4

    Calculo = TotalMinLlegada - TotalMinSalida
    RESTOalHotel = Calculo - 45
    CambiarCalculoAHora = RESTOalHotel//60
    CambiarCalculoAMinuto = RESTOalHotel % 60

    print(f"Tarda el Avion un total de {CambiarCalculoAHora} de horas y un total de {CambiarCalculoAMinuto} de minutos")
