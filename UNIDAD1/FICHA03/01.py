# 1. Plazo fijo
'''Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente
 de un banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado
  era de 2.3% y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.'''
import PySimpleGUI as psg

capital = float(psg.popup_get_text("Bienvenido al simulador de plazo fijos\n\tIngrese monto a invertir: ","Banco"))
intereses = float(1.023)
gastos = int(20)
saldo_final = round(capital*intereses - gastos , 2)

psg.popup("Banco" ,"El saldo de su inversion sera: " , saldo_final)
