#Valida la longitud de una palabra 

#palabra = input("Introduce una palabra: ")

#if len(palabra) >= 4 and len(palabra) <= 8:
#    print("La palabra " +palabra+ " es correcta")
#elif len(palabra) < 4:
#    print("Hacen falta letras. Solo tienen " + str(len(palabra))+ " letras" ) 
#elif len(palabra) > 8:
#    print("Sobran letras. Tiene " + str(len(palabra)) + " letras")

print("\nIdentificacion de cuadrantes\n")

while True : 
    try :
        numero_uno = int(input("Escribe el primer numero "))
        break
    except ValueError :
        print("numero incorrecto, vuelve a escribir un numero")
        continue

