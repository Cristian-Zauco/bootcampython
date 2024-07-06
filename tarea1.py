#Define los mensajes de encabezado para realizar una modificacion mas agil al momento de cambiar texto
mensaje_encabezado="********** Calcular su IMC 'Indice de masa corporal' **********"
mensaje_indicador="Por Favor en el siguiente formulario debera ingresar sus datos para realizar el calculo"


#Imprime mensaje de encabezado
print(mensaje_encabezado.title())

#Imprime mensaje indicativo
print(mensaje_indicador)

#Toma de datos de la persona 
print("Ingrese su nombre: ")
nombre = input()
if (len(nombre)<=3):
        print("El nombre que ha ingresado es incorrecto o muy corto, ingrese su nombre correcto")

print("Ingrese su apellido paterno: ")
apellido_paterno = input()
if (len(apellido_paterno)<=3):
        print("El nombre que ha ingresado es incorrecto o muy corto, ingrese su apellido paterno correcto")

print("Ingrese su apellido materno: ")
apellido_materno = input()
if (len(apellido_materno)<=3):
        print("El nombre que ha ingresado es incorrecto o muy corto, ingrese su apellido materno correcto")

print("Ingrese su edad: ")
edad = input()
if type(edad) != int:
    print('Ingrese su edad en valor numerico')

print("Ingrese su edad: ")
peso = input()
if type(peso) != int or type(peso) != float:
    print('Ingrese su peso en valor numerico')


if not type(edad) is int:
  raise TypeError("No permite valores numericos") 