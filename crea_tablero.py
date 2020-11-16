
def cambia_digito(digito):
    if digito == 1:
        return 8
    elif digito == 2:
        return 7
    elif digito == 3:
        return 6
    elif digito == 4:
        return 5
    elif digito == 5:
        return 4
    elif digito == 6:
        return 3
    elif digito == 7:
        return 2
    elif digito == 8:
        return 1
    elif digito == 9:
        return 0
    elif digito == 0:
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
    auxiliar = 0

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
tablero = actualiza(tablero,[1,2,3,4,5,6])
muestra_tablero(tablero)
tablero2 = crea_tablero()
tablero2 = actualiza(tablero2,[0,1,2,3,4,5])
muestra_tablero(tablero2)
tablero3 = crea_tablero()
tablero3 = actualiza(tablero3,[0,0,1,2,3,4])
muestra_tablero(tablero3)
tablero4 = crea_tablero()
tablero4 = actualiza(tablero4,[0,0,0,1,2,3])
muestra_tablero(tablero4)
tablero5 = crea_tablero()
tablero5 = actualiza(tablero5,[0,0,0,0,1,2]) #falló
muestra_tablero(tablero5)
tablero6 = crea_tablero()
tablero6 = actualiza(tablero6,[0,0,0,0,0,1])
muestra_tablero(tablero6)


