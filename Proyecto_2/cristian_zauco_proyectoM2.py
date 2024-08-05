#Importacion del modulo time
import time

#Variable global de salto de linea 
salto_linea = "\n"
#Solicitud de la palabra o dato a evaluar
palabra = input("Introduce una palabra: ")

"""
Validacion de la longitud de la palabra por medio de condicionales
"""

if len(palabra) >= 4 and len(palabra) <= 8:
    print("La palabra " +palabra+ " es correcta")
elif len(palabra) < 4:
    print("Hacen falta letras. Solo tienen " + str(len(palabra))+ " letras" ) 
elif len(palabra) > 8:
    print("Sobran letras. Tiene " + str(len(palabra)) + " letras")

#Mensajes en pantalla 
print(salto_linea + "Identificacion de cuadrantes" + salto_linea)
print("para identificacion de cuadrantes exactos no debes escribir el numero 0" + salto_linea)

"""
Declaracion de variables y colecciones
"""
numeros_no_permitidos = 0
cuadrantes = ["El cuadrante es : I", "El cuadrante es : II", "El cuadrante es : III", "El cuadrante es : IV"]

"""
Solicitud de datos donde se evalua que el dato ingresado sea un numero y
el numero ingresado sea diferente de 0 
"""
while True :
    try:
        numero_uno = int(input("Escribe el primer numero X: "))
        if numero_uno == numeros_no_permitidos :
            print("No puedes escribir el numero 0 volver a iniciar")
            break
        break
    except ValueError :
        print("Error: Escribe un numero correcto")
        continue

while True :
    try:
        numero_dos = int(input("Escribe el segundo numero Y: "))
        if numero_dos == numeros_no_permitidos :
            print("No puedes escribir el numero 0 volver a iniciar")
            break
        break
    except ValueError :
        print("Error: Escribe un numero correcto")
        continue

"""Llama una coleccion de datos llamada cuadrantes evaluando los numeros 
ingresados por el usuario en pantalla"""

if numero_uno > 0 and numero_dos > 0 :
    print(salto_linea + cuadrantes[0])
elif numero_uno < 0 and numero_dos > 0 :
    print(salto_linea + cuadrantes[1])
elif numero_uno < 0 and numero_dos < 0 :
    print(salto_linea + cuadrantes[2])
elif numero_uno > 0 and numero_dos < 0 : 
    print(salto_linea + cuadrantes[3])

"""Mantiene el tiempo en pantalla de ejecucion antes de terminar
con el fin de validar la salida del resultado"""
time.sleep(5.5)

