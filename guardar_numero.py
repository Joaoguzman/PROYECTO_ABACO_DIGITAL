
'''
Haga un programa que muestre una cantidad ingresada por el usuario en
forma de abaco en pantalla
** Use buenas practicas de programación en python pep8
'''
#funcion que valida la entrada del usuario aceptando
#solo digitos y no caracteres.
#debe retornar el numero o string que ingresó el usuario
#def solo_digitos():
    
#funcion que toma el numero ingresado por el usuario y lo 
# descompone en las unidades que necesita el abaco.
# unidad | decena | centena | unidad de 1.000 | unidad de 10.000
# unidad de 100.000
# debe retornar todas estas variables.
#def descompone_numero():
    
#Funcion que muestra en pantalla el dibujo del abaco segun el numero ingresado
#def actualiza_tablero(numero):

#funcion que aplica el punto separador de miles para mostrar
#la cifra con claridad
# *** debe retornar el resultado de la conversión


def convertir_numero(numero): 
	return ("{:,}".format(numero)).replace(",", ".")

print(convertir_numero(100000)) 

#def guardar_numero(numero)
'''
seq = (numero)
dict = dict.fromkeys(seq)
print("Números Ingresados: %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print("Números Ingresados: %s" %  str(dict))
'''
	
def guardar_numero(numero):
  for n in numero:
    print(n)

numero = ["1", "2", "3", "4"]

guardar_numero(numero)	
