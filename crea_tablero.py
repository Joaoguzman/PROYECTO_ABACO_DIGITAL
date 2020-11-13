
def conversor_monto_abaco(monto):
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

#numero = int(input("Ingrese un numero"))

#monto = conversor_monto_abaco(numero)
monto = conversor_monto_abaco(4)

def crea_tablero():
    lista_abaco = []
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
        lista_abaco.append(abaco)
        contador +=1
    return lista_abaco

lista_abaco = crea_tablero()

for i in range(0,11):
    for j in range(0,6):
        print(lista_abaco[j][i], sep="", end="")
    print()