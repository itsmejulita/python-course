#El pop se utiliza para recortar el ultimo elemento de una lista 
edades = [41, 37, 22, 20, 38, 48, 34, 33, 36] 
mi_edad = 21 
edades.append(mi_edad) #añadimos un valor a la lista 
# edades [0] = 26
# edades [0:3] = []
print (edades)
edades.pop ()
# print (edades)
edades.pop (0)
print (edades)
indice = 2
edades.pop (indice)
print("el elemento eliminado de la lista es", edades) 
#count + index
numeros = [1,1,1,4,2,1,4,1]
veces_1 = numeros.count(4) # El count indica la cuantas veces hay un elemento en una lista 
print (veces_1) 
indice = numeros.index(4) # El index indica la posicion (el indice) del elemento 
print ("el indice del elemento 4 es", indice)

#ver los bool urgent
#tuplas 
