# numero = 0
# while numero <10: 
#     numero += 1 
#     print (numero)


#     #############################
#     #DICCIONARIO
#     ############################

# #1 Crear dos variables una que se llame user y otra password 


# def almacenar (data): 

# Bucle FOR 
"""
numeros = [1, -3, 4, 2, -5]
for i in numeros:
    print (i)

lista = [1, "Men", 22, "soda"]
for i in lista: 
    print (lista)
"""

# Range 
"""
for x in range(0,101,5):
    if x%15 == 0:
        print(x)

for x in range (0,10,20):
    if x%5 == 0:
        print (x)


for x in range(0,101):
  if x % 10==0:
    print(x)

# Imprime todos los numeros impares del 1 al 10 

for numero in range (1,10):
   if numero % 2 !=0: 
      print (numero)
for numero in range (1,20):
   if numero % 5 == 0:
      print (numero)
"""
# For in Range 

cantidad = int(input("Ingrese un numero entre el 1 y el 5: "))
if cantidad == 1:
    print ("hola")
elif cantidad == 2:
  for x in range (2):
    print ("Hola!!")
elif cantidad == 3:
   for x in range (3):
      print ("Hola, qué tal Juliana")
elif cantidad == 4:
    for x in range (4):
       print ("Hola Juliana Fenoglio") 
elif cantidad == 5: 
   for x in range (5):
      print ("Hola Juliana Fenoglio, como estas? ")
else: 
   print ("Has ingresado un numero no correspondiente, intente de nuevo.")
palabra = "Juliana"
for x in enumerate (palabra): 
    print (x)

# Suma 
"""
lista = []
for i in range (5): 
    num = int(input("Ingrese un numero: "))
    print ("El numero que has ingresado es:", num) 
lista.append (num)
print ("Hemos guardado  el número: ")
print (lista)
"""

# Bucle While 

edad = 13
while edad <=21:
    print("Eres menor de edad, tu edad es ", edad)
    edad += 2
    print ("Tanto tiempo!!")

num = 3
while num >0:
    print(f"{num}")
    num-=1
    print ("Termino el conteo")
# Preguntar la edad pero queremos validar que sea una edad real 
while True:
    edad = int(input("Ingrese la edad: ")) 
    if 0<=edad<=99:
        break
    elif edad ==-1: 
        break
    else:
        print ("Por favor ingrese un valor correcto: ")
print ("Gracias por ingresar un valor correcto, la edad ingresada es: ", edad)

i = 0
while i<6:
    i+=1
    if i == 3:
        continue
    print (i)
x = 1
while x<6:
    x+=1
    if x ==4:
        continue
    print (x)









    









