# Programa verificar si un número es palíndromo.(Se lee igual al revés)
 
# controlamos lo que introduce el usuario.
try:
    nun_pal = int(input("Introduce un número y te dire si es palíndromo. "))
    num = str(nun_pal)
    if nun_pal < 0 :
        print("Este número no es palíndromo")
    elif num == num[::-1] :
        print("Este número es palíndromo")
    else:
        print("Este número no es palíndromo")
except:
    print("Debes introducir un número.")
