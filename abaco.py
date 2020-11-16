import funciones as abaco


print("Bienvenido al Ábaco Digital\n Para salir digite -> salir")
print("")

#Creando un tablero vacío
tablero = abaco.crea_tablero()

#Creando historial
historial = abaco.crea_historial()

estado = " "
while estado != "salir":
    numero = abaco.solo_digitos() 
    if numero != "salir":
        mi_numero = abaco.descompone_numero(numero)
        tablero = abaco.actualiza(tablero, mi_numero)
        abaco.muestra_tablero(tablero)
       #Funcion que retorna numero con punto separador de miles
        guarda_numero = abaco.convertir_numero(numero)
        historial = abaco.guardar_numero(guarda_numero, historial)
        
    elif numero == 'salir':
        estado = "salir"

#Funcion para mostrar historial
abaco.muestra_historial(historial)
    


