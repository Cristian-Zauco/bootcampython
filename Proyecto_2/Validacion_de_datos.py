palabra = input("Introduce una frase: ")

if len(palabra) >= 4 and len(palabra) <= 8:
    print("La palabra " +palabra+ " es correcta")
elif len(palabra) < 4:
    print("Hacen falta letras. Solo tienen " + str(len(palabra))+ " letras" ) 
elif len(palabra) > 8:
    print("Sobran letras. Tiene " + str(len(palabra)) + " letras") 





