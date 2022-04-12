import PySimpleGUI as psg
pasword = "uTn2022"

nombre = psg.popup_get_text("Ingrese su nombre:", "Identificación")

verification = psg.popup_get_text("Ingrese su clave:", "autenticacion")

while pasword != verification :
     print(psg.popup("Inicio", "Clave incorrecta\n inserte nuevamente su clave"))
     verification = psg.popup_get_text("Ingrese su clave:", "autenticacion")
else:
      print(psg.popup("Inicio", "Le damos la bienvenida...", nombre))

