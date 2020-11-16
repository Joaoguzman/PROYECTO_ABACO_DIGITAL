import funciones as abaco

<<<<<<< HEAD

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
    


=======
** Use buenas practicas de programación en python pep8
'''
#funcion que valida la entrada del usuario aceptando
#solo digitos y no caracteres.
#debe retornar el numero o string que ingresó el usuario
def solo_digitos():
    pass
#funcion que toma el numero ingresado por el usuario y lo 
# descompone en las unidades que necesita el abaco.
# unidad | decena | centena | unidad de 1.000 | unidad de 10.000
# unidad de 100.000
# debe retornar todas estas variables.
def descompone_numero():
    pass
#Funcion que muestra en pantalla el dibujo del abaco segun el numero ingresado
def actualiza_tablero(numero):
    pass
#funcion que aplica el punto separador de miles para mostrar
#la cifra con claridad
# *** debe retornar el resultado de la conversión
def convertir_numero(numero):
    pass
#Funcion que guarda el numero con punto en un diccionario
# **Este debe retornar un diccionario
def guardar_numero( ):
    pass
    

print("Bienvenido al Ábaco Digital\n Para salir digite -> salir")

numero = " "
while numero != "salir":
    numero = input("Ingrese un numero: ")
    
    if numero.isdigit():
        print("Su numero es: ", numero)
    elif numero == 'salir':
        numero = "salir"
    else:
        print("No es un numero")
        print("Intenta nuevamente!")
>>>>>>> 8db0974e02a20e15396b460f89420bb7346dc884
