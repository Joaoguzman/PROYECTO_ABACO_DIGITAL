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
    marcador = ["cm","dm","mi","ce","de","un"]
    lista_abaco = {}
    contador = 0
    while contador!=6:
        abaco = [] #string que creará el dibujo
        for estado  in range(0,11): # for que crea un abaco vacio
            if estado == 0 :
                abaco.append("     +-+    ") 
            elif estado == 10:
                abaco.append("     {}     ".format(marcador[contador]))  
            elif estado >=1 and estado <=9:
                abaco.append("     | |    ")   
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
    marcador = ["cm","dm","mi","ce","de","un"]
    cont_numero = 0

    for clave in range(0,len(numero)):
        abaco = []
        for estado in range(0,11):
            if estado == 0 :
                abaco.append("   +-+  ")
            elif estado == 10:
                abaco.append("   {}   ".format(marcador[cont_numero]))  
            elif estado >=1 and estado <=cambia_digito(numero[cont_numero]):
                abaco.append("   | |  ")
            else:
                abaco.append("  ##### ")
        cont_numero = cont_numero + 1
        diccionario[clave] = abaco
    return diccionario


def solo_digitos():    
    while True:
        numero_original = input("Ingrese un número sin puntos: ")    
        try:        
            numero_original = int(numero_original)        
            if numero_original >= 0 and numero_original <= 999999:            
                return numero_original        
            else:            
                print("Ingrese un número entre 0 y 999.999")    
        except ValueError:        
            if numero_original == "salir":
                return "salir"
            else:
                print("Ingresa un número. No letras ni puntos.")

def descompone_numero(numero_original):    
    lista_digitos = [0, 0, 0, 0, 0, 0]    
    numero_original = str(numero_original)    
    for digito in numero_original:        
        lista_digitos.append(int(digito))    
        while len(lista_digitos) != 6:        
            lista_digitos.pop(0)         
    return lista_digitos    


def convertir_numero(numero): 
	return ("{:,}".format(numero)).replace(",", ".")

def guardar_numero(numero, lista):
    lista.append(numero)
    return lista

def crea_historial():
    lista=[]
    return lista

def muestra_historial(historial):
    print("Estos son sus números: ")
    for element in historial:
        print(element)
        