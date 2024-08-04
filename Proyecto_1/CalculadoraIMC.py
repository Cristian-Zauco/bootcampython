import os
#Define los mensajes de encabezado para realizar una modificacion mas agil al momento de cambiar texto
mensaje_encabezado="********** Calcular su IMC 'Indice de masa corporal' **********"
mensaje_indicador="Por Favor en el siguiente formulario debera ingresar sus datos para realizar el calculo"
espacio_blanco=" "
#Imprime mensaje de encabezado
print(mensaje_encabezado)

#Imprime mensaje indicativo
print(mensaje_indicador)

#Toma de datos de la persona 
nombre = str(input("Escribe tu nombre: "))
while len(nombre) <= 2:
    nombre = str(input("Error: Escribe tu nombre correcto"))

apellido_paterno = str(input("Escribe tu apellido paterno: "))
while len(apellido_paterno) <= 2 :
    apellido_paterno = str(input("Error: Escribe tu apellido paterno correcto "))

apellido_materno = str(input("Escribe tu apellido materno: "))
while len(apellido_materno) <= 2 :
    apellido_materno = str(input("Error: Escribe tu appellido materno correcto "))

#Ingreso de edad
while True :
    try:
        edad = int(input("Escribe tu edad: "))
        break
    except ValueError :
        print("Error: Escribe tu edad correcta")
        continue

#Ingreso de peso 
while True :
    try :
        peso = float(input("Escribe tu peso: "))
        break
    except ValueError :
        print("Error: Escribe tu peso correcto")
        continue

#Ingreso de estatura 
while True :
    try :
        estatura = float(input("Coloque su estatura: "))
        break
    except ValueError :
        print("Error: Estatura incorrecta")
        continue

#Calculo de IMC
InMaCo = peso / estatura**2

#Evalua estatus IMC
if InMaCo >= 0 and InMaCo<=15.99 :
    mensajeIMC = "Delgadez severa"
elif InMaCo >= 16.00 and InMaCo <= 16.99 :
    mensajeIMC = "Delgadez moderada"
elif InMaCo >= 17.00 and InMaCo <= 18.49 :
    mensajeIMC = "Delgadez leve"
elif InMaCo >= 18.50 and InMaCo <= 24.99 :
    mensajeIMC = "Normal"
elif InMaCo >= 25.00 and InMaCo <= 29.99 :
    mensajeIMC = "Sobrepeso"
elif InMaCo >= 30.00 and InMaCo <= 34.99 :
    mensajeIMC = "obesidad leve"
elif InMaCo >= 35.00 and InMaCo <= 39.00 :
    mensajeIMC = "obesidad media"
elif InMaCo >= 40.00:
    mensajeIMC = "obesidad morbida"

#limpia pantalla de datos ingresados
os.system('cls' if os.name == 'nt' else 'clear')

#Impresion de datos finales
print("¡Hola! " + nombre + espacio_blanco + apellido_paterno + espacio_blanco + apellido_materno + 
      "\ntu edad ingresada es: " + str(edad) + "\ntu peso ingresado es: " + str(peso) + "\ntu estatura ingresada es: "
      + str(estatura) + "\ntu IMC es: " + str(InMaCo) + "\nBajo los indicadores tiene: " + mensajeIMC)
