
def cambia_digito(monto):
    if monto == 1:
        return 8
    elif monto == 2:
        return 7
    elif monto == 3:
        return 6
    elif monto == 4:
        return 5
    elif monto == 5:
        return 4
    elif monto == 6:
        return 3
    elif monto == 7:
        return 2
    elif monto == 8:
        return 1
    elif monto == 9:
        return 0
    elif monto == 0:
        return 10

def crea_tablero():
    lista_abaco = {}
    contador = 0
    while contador!=6:
        abaco = [] #string que creará el dibujo
        for estado  in range(0,11): # for que crea un abaco vacio
            if estado == 0 :
                abaco.append("   +   ") 
            elif estado == 10:
                abaco.append("   +   ")    
            elif estado >=1 and estado <=9:
                abaco.append("  | |  ")    
            else:
                abaco.append("#######")
        lista_abaco[contador] = abaco
        contador +=1
    return lista_abaco

def muestra_tablero(tablero):
    for i in range(0,11):
        for j in range(0,6):
            print(tablero[j][i], sep="", end="")
        print()

def actualiza(diccionario,numero):
    cont_numero = 0
    for clave in range(0,len(numero)):
        abaco = []
        for estado in range(0,11):
            if estado == 0 :
                abaco.append("   +   ") 
            elif estado == 10:
                abaco.append("   {}   ".format(numero[cont_numero]))    
            elif estado >=1 and estado <=cambia_digito(numero[cont_numero]):
                abaco.append("  | |  ")
            else:
                abaco.append(" ##### ")
        cont_numero = cont_numero + 1
        diccionario[clave] = abaco
    return diccionario


tablero = crea_tablero()
muestra_tablero(tablero)
print()
tablero = actualiza(tablero,[1,9,8,7,6,5])
muestra_tablero(tablero)
