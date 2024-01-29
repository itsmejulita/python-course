# #Este ejercicio le tenemos que agregar al ultimo indice del corchete la suma de los valores dados
# matriz1 = [[1,5,1], 
# [2,1,2],
# [3,0,1],
# [1,4,4]] 
# v1 = [sum(matriz1[0])]
# v2 = [sum(matriz1[1])]
# v3 = [sum(matriz1[2])]
# v4 = [sum(matriz1[3])]

# matriz2 = [matriz1[0]+v1,
# matriz1[1]+v2,
# matriz1[2]+v3,
# matriz1[3]+v4] 
# # print (matriz2)
# #######################
# #######################
# partidos_ganados = int(input("ingrese la cantidad de partidos ganados"))
# partidos_empatados = int(input("ingrese la cantidad de partidos empatados"))
# partdos_perdidos = int(input("ingrese la cantidad de partidos perdidos"))
# total = partidos_ganados*3+partidos_empatados*1+partdos_perdidos*2 
# # print ("El promedio total de partidos son", total/20) 

# numero1 = 9
# numero2 = 3
# numero3 = 6
# media = (numero1+numero2+numero3)
# mitad = (media/3)
# #print ("la nota media es", mitad) 
#-------
# Condicionales if, else y elif 
# Crear un programa para saber si un numero ingresado es par o impar 

# numero = int(input("ingrese un numero: "))
# if numero % 2 == 0: # El % (modulo) se utiliza para calcular el resto de una division 
#     print ("el numero es par", numero) 
# else: 
#     print ("el numero es impar", numero) 

#--------
# Crear un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no 
# Si el usuario tiene entre 14-17 años es adolescente 
# Y si el usuario tiene entre 5-13 años es niño 

# edad = int(input("¿Cuantos años tenes?: "))
# if edad <=14: 
#     print ("Eres menor de edad") 

# elif edad >=14 and edad <=17:
#     print ("Eres adolescente")

# else: 
#     print ("Eres mayor de edad :))) ")
#-------
# Crear un programa que guarde una contraseña en una variable 
# Pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
#que introduce el usuario coincide con la guardada en la variable 

# clave_por_defecto = "itsmejulita123"
# clave_del_usuario = input("Ingrese la contraseña: ")
# if clave_por_defecto == clave_del_usuario: 
#     print (clave_por_defecto0) 
# else: 
#     print ("la contraseña no coincide, intente nuevamente: ")

#-------
#------- Ejercicio 1
# numero1 = int(input("Ingrese un numero"))
# numero2 = int(input("ingrese otro numero"))
# if numero1>numero2:
#     print("el numero mayor es :", numero1)
# elif numero2>numero1:
#     print("el numero mayor es: ", numero2)
# else:
#     print ("Los numeros son iguales") 
#------ Vamos con el ejercicio 2 ¡¡¡NO TERMINADO!!!
# def crear_usuario ():
#     usuario = input("ingresa nombre de usuario: ")
#     contraseña = input("ingresa una contraseña: ")
# while len(contraseña) >8 : 
#     print ("la contraseña debe tener al menos 8 caracteres")
#     contraseña = input("ingresa tu contraseña: ")
# print (usuario and contraseña)  

#------ Ejercicio 6 
# numero1 = int(input("Ingrese el primer numero: "))
# numero2 = int(input("Ingrese el segundo numero: "))
# numero3 = int(input("Ingrese el tercer numero: "))
# Falta de terminar. !!!! Ejercicios de Coderhouse
#--------
#-------- EJERCICIOS DE APRENDE CON ALF:
usuario = input("Hola usuario, introduzca su nombre")
#print ("Hola", usuario) 
operacion = (((3+2) / (2*5))**2)
#print (operacion) 
horas = float(input("Introduzca el numero de horas que trabaja: "))
coste = float(input("Introduzca el coste por hora"))
paga = horas * coste
#print ("Tu paga es de:", paga) 
n = ()
numero = int(input("Introduzca un número entero: "))
suma = numero * (numero+1) /2
#print ("La suma de los primeros numero enteros desde 1 hasta" + str(numero) + "es" + str(suma))
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = round(float(peso)/float(altura)**2,2) 
#print ("Su indice de masa corporal es de: ", imc) # donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.






















