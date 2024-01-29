# Operadores y expresiones 
#------
#------
#booleano (binario) -- solo tiene 2 opciones: True - False
x = True  # Variable de type bool 
y = False # Variable de type bool 

expresion1 = (1+1==2) # ¿1+1 es igual a 3? == de comparación
#print (expresion1)  
expresion2 = (2>4)  # ¿es 2 mayor que 4? puedo usar simbolos > o <
#print (expresion2) 
#¿es 1+1 igual a 2 Y TAMBIÉN es 2 mayor a 4?
expresion3 = (1+1 == 2 and 2>4)
#print (expresion3)
expresion4 = (2+2 == 4 and 3**2 == 9)
#print (expresion4)
#------
#------
edad = int(input("Ingrese la edad de tu profesor"))
expresion5 = (edad >= 27) # Valor booleano
print ("La edad es mayor a 27", expresion5)  
#------
#------
j = 17
expresion5 = (17<=j<=20) # En este caso, la expresión retornará True,
                        #si el valor de c es mayor o igual a 13 y menor o igual a 20. 
print (expresion5)
expresion5 = (13<=j) and (j<=20) 
print (expresion5)
expresion5 = (j!=16) #¿j es distinto de 16? True 
print (expresion5)
edades = [22, 25, 29]
print (not len(edades) ==4) #criterio para usar estos operadores (and,or,not)
# Es True porque efectivamente la lista no contiene 4 elementos.

# Operadores Relacionales 
expresiones = [False == True,
               10>=2*4,
               33/3 == 11,
               True > False,
               True*5 == 2.5*2]
print (expresiones) 

# Operadores lógicos (and,or,not)
x = not True 
print (x)
y = not True == False 
print (y) 

#------
#------
U = input("Ingrese su numero de usuario")
C = int(input("ingrese su contraseña"))
