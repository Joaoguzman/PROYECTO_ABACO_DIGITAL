#funcion que toma el numero ingresado por el usuario y lo 
# descompone en las unidades que necesita el abaco.
# unidad | decena | centena | unidad de 1.000 | unidad de 10.000
# unidad de 100.000
# debe retornar todas estas variables.
def descompone_numero(numero_original):
    lista_digitos = [0, 0, 0, 0, 0, 0]
    numero_original = str(numero_original)
    for digito in numero_original:
        lista_digitos.append(digito)
    unidad = int(lista_digitos[-1])
    decena = int(lista_digitos[-2])*10
    centena = int(lista_digitos[-3])*100
    mil = int(lista_digitos[-4])*1000
    diez_mil = int(lista_digitos[-5])*10000
    cien_mil = int(lista_digitos[-6])*100000
    return print(cien_mil, diez_mil, mil, centena, decena, unidad)
numero_original = int(input("Numero original: "))
descompone_numero(numero_original)
