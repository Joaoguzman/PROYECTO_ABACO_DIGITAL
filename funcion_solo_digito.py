#funcion que valida la entrada del usuario aceptando
#solo digitos y no caracteres.
#debe retornar el numero o string que ingresó el usuario
def solo_digitos():
    numero_original = input("Ingrese un número sin puntos: ")
    try:
        numero_original = int(numero_original)
        if numero_original <= 999999:
            print("Numero ", numero_original, "ingresado")
    except ValueError:
        print("Ingresa un número. No letras ni puntos.")
    return numero_original

solo_digitos()