#listas --- mutable si , orden si
#tuplas --- mutable no , orden si
#conjuntos - mutable si, orden no

conjunto1 = {1,1,1,1,2,3,4,4,4,2,2,2,3,3}
print(conjunto1) 

#conversion entre listas (list), tuplas (tuple) y conjuntos(set)

numeros = [1,1,1,2,2,3,5,5,5,4,23,11]
# Vamos a convertir de lista a tupla 

numeros_tupla = tuple(numeros)

nombres = ("Juan", "Maria", "Juliana", "Gimena", "Rosario")
# Vamos a convertir de lista a tupla 

nombre_lista = list(nombres)
print (nombre_lista)
# Vamos a convertir de lista a conjunto (Eliminar los elementos repetidos)

numeros_conjunto = set(numeros)
print (numeros_conjunto)

#luego, si deseo, puedo volver a pasarlo a lista

numeros = list(numeros_conjunto)
print (numeros)
#add
numeros_conjunto.add(30)
print(numeros_conjunto)

#update
numeros_conjunto = set() # Un conjunto vacio 
numeros_conjunto.update([1,2,3])
print(numeros_conjunto)
#len

print(len(numeros_conjunto)) #cantidad de elementos
# Discard
# Eliminar (descartar) un elemento del conjunto 
numeros_conjunto.discard("t")
numeros_conjunto.discard(2000)
print(numeros_conjunto)
conjunto7 = {9,23,"hola", "pyhton", 13}
conjunto7.discard ( "chau") 
conjunto7.discard ("13")
print (conjunto7)
# Remove 
# Eliminar (remover) un elemento del conjunto 
numeros_conjunto.remove(2)  #Si quisiera remover un elemento que NO EXISTE, tenemos ERROR
print(numeros_conjunto)
conjunto7 = {9,23,"hola", "pyhton", 13}
if "chau" in conjunto7:
    print ("El elemento si se encuentra en el conjunto: ") #Elimina el elemento 
else:
    print ("El elemento no se encuentra en el conjunto: ")
#------ El mismo solo que con diferente elemento 
conjunto7 = {9,23,"hola", "pyhton", 13}
if "hola" in conjunto7:
    print ("El elemento si se encuentra en el conjunto: ") #Elimina el elemento 
else:
    print ("El elemento no se encuentra en el conjunto: ")
#in -- elemento está dentro o no del conjunto (elemento in conjunto)
23 not in conjunto7 #si el elemento 23 esta dentro del conjunto llamado conjunto7 ????

#clear -- eliminar todos los elementos
#conjunto7 = set() #conjunto vacio es set()
conjunto7.clear()

print (conjunto7)

conjunto8 = {9, 23, "hola", "python", 13, 2.12, True}
while len(conjunto8)>6:
    eliminado = conjunto8.pop() #pop elimina al azar y al mismo tiempo te da el valor que ha eliminado, pop da un resultado
print ("Se ha eliminado el elemento", eliminado)
print ("El conjunto queda de la siguiente manera: ", conjunto8) 

############# EJERCICIOS DE LA CLASE 8 MANEJO DE ARHIVOS Y DATOS 
diccionario2 = {"vasos": 8 ,"platos" : 50 ,"cubiertos" : 90}
print (diccionario2["platos"])
mi_dic = {"rosa": 24.2, "maria": "29", 0:[33, "python", True], "ernesto":{"A":"B"}}
print (len(mi_dic))
#Acceder a un dato (pareja key:value) --- keys pueden usar datos inmutables (enteros string)
print ("La edad que está vinculada al key 0 es: ", mi_dic[0])
print ("La edad que está vinculada al key ernesto es: ", mi_dic["ernesto"])
#Keys 
print (tuple(mi_dic.keys())) # Mostrará solamente los keys, los podes convertir a listas o tuplas 
print ("Las keys que están creadas dentro de mi diccionario son: ")
for k in mi_dic.keys(): 
    print(k)
    
#Values
print (mi_dic.values())
print("Los valores de mi diccionario son: ")
for v in mi_dic.values():
    print(v)
#/////
colores = {"amarillo": "yelow", "azul": "blue", "verde": "green"}
#Correspondiente al key azul 
print(colores["azul"])

#Get tambien te da el value correspondiente al key ingresado! #-- Sirve para acceder a un valor en un diccionario
print (colores.get("amarillo", "No hay dicha clave!!!" )) #Si existe la key retorna el value, si no existe manda un mensaje
print (colores.get("blanco", "No hay dicha clave!!!" ))
#enumerate --- (indice, valor)  ---
for x in enumerate (["lunes", "martes", "jueves"]):
    print(x)
#items --- (key, value)
for x, y in colores.items():
    print("Para la clave: ", x, "el valor es: ", y)
for elemento1, elemento2, elemento3, in [(1,2,3), ("hola", "chau", "fin"), (True, False, None)]:
    print(elemento3)

















