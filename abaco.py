import funciones as abaco


print("Bienvenido al Ábaco Digital\n Para salir digite -> salir")

#Creando un tablero vacío
tablero = abaco.crea_tablero()

#Creando historial
historial = abaco.crea_historial()

estado = " "
while estado != "salir":
    numero = abaco.solo_digitos()
    
    if numero != "salir":
        print("Su numero es: ", numero)
    elif numero == 'salir':
        estado = "salir"
    


