#Vamos a trabajar lo que son las listas y las tuplas mediante el contenido de python 
#Las listas se escriben entre corchetes for example 
""" # Listas con numeros y str
numeros = [1,2,3,4]  
print (numeros)

otra_lista = ["hola", "como", "estas", "?"]
print (otra_lista)

#LISTAS Y STRINGS (STR), ACÁ VEMOS LA CONCATENACIÓN con + 

datos= [1, -5, 6, "una cadena", "otra cadena"] 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
unir_listas = lista1 + lista2

print (unir_listas) 
lista3 = ["manzanas", "uvas", "bananas"]
unir_listas = lista1 + lista2 + lista3
print (unir_listas) 
"""

# Listas con la funcion APPEND 
"""
paises = ["Argentina", "Brasil", "Rusia"]

print ("El país que mas me gusta es:", paises[0]) 

recomendación = input ("Dime un pais para visitar el priximo año") # pedimos un str
print (recomendación)
paises.append (recomendación) 

# A la lista paises le agregamos una recomendación que vendria a ser la funcion APPEND  

print (paises)
"""
"""
# Mas examples con la function APPEND 
numeros = [1, 2, 3, 4, 5]
numeros.append (5)
#print (numeros)
usuario = ["nombre", "contraseña", "dni"]
usuario.append ("edad")
print (usuario) 

numeros = [1, 2, 3, 4, 5]
numeros.append (3*2+10)
print (numeros)
len(numeros)
print (numeros)
"""

""" # Ejemplos de listas 
lista = ["lapiz" , "colores" , 85 , "ingles" , 6 , "profesora"] 
print (lista[::3])
print (lista[::2])
print (lista[::-1])
"""

""" # Listas con la funcion [:]
lista = [1, 2 , 3 , 4 , 5 , 6]
print (lista[::5])  

# La función [::-1] en Python se utiliza para invertir el orden de una secuencia, como una lista o una cadena.
# :: es la sintaxis de Python para “slicing”, que es una forma de obtener subconjuntos de una secuencia.
# ::3 for example especifica el paso, es decir, cuántos elementos avanzar después de cada elemento que se toma.

lista = [1, 2 , 3 , 4 , 5 , 6]
print (lista[::3])


#supongamos que tenemos la siguiente lista y queremos tomar los ultimos 3 numeros de ella 
a = [0, 1, 2, 3, 4, 5, 6]  
ultimos_3 = a[-3:] 
print (ultimos_3) 
"""

""" # Listas heterogeneas


letras = ["a", "b", "c", "d", "e", "f"]
letras[:3] = ["A", "B", "C"]
print (letras) 
letras = [] # De esta manera eliminamos todos los elementos de una lista 
print (letras)
""" 
#########################
#########################
# TUPLAS 
numeros2 = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 7, 2, 11, 15, 9, 355) #La tupla tiene parentesis 
# Paso 1
print (numeros2[-1]) # Los indices tambien funcionan en tuplas [indice]
# Paso 2
print (len(numeros2)) # Muestra la cantiada de elementos que hay en una tupla 
# Paso 3 
print (numeros2.index(87)) # Devuelve el indice del elemento 87
# Paso 4 
print (numeros2[8]) # Muestra el elemnto correspondiente a la posicion 8 
# Paso 5 
print (numeros2.count(7)) # Cuenta la cantidad de veces que se repite un elemento 

edades = (41, 37, 22, 20, 38, 48, 34, 33, 36)
mi_edad = 27

#edades.append(mi_edad) #NO PERMITE añadir un valor nuevo (inmutables)
#edades[0:3] = (26, 23, 12) #NO PERMITE modificar los valores del indice 0 al 2 (INMUTABLE)

#edades.pop() #NO PERMITE eliminar elementos (INMUTABLE)

print(edades)









