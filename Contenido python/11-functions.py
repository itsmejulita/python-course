# variable_test = 10 

# def test(): 
#     variable_test = "mates"
#     print (variable_test)

# test () 
#####################
#####################
#
# def saludar_con_nombre (nombre): 
#     saludando = print ("buen dia, como estas? " + nombre)
#     return saludando 

# saludar_con_nombre ("pedro")
######################################
def saludar_con_nombre (nombre): 
    saludando = nombre
    return saludando 

print (saludar_con_nombre ("pedro")) 

def crear_animal (patas,tipo):
    animal = print ("acabo de crear un " + tipo + "de " + str(patas) + " patas ") 
    return animal 

crear_animal (4, "vaca")
crear_animal(2, "gallina")

def crear_un_auto (marca,ruedas,puertas): 
    automovil = print ("invente un auto con " + str(ruedas) + " ruedas, es de marca " + marca + " y tiene " + str(puertas) + " puertas") 
    return automovil 

crear_un_auto ("ferrari", 4, 2)
crear_un_auto ("ford ka", 5, 5) 
##############################################
##############################################

def mi_calculadora (numeros,numeros2,operaciones): 

    if operaciones == "suma": 
        resultado = numeros + numeros2

        return resultado 
    
    elif operaciones == "multiplicacion": 
        resultado = numeros * numeros2
        return resultado 
    elif operaciones == "division":
        resultado = numeros / numeros2
        return resultado 
    
    
    
print (mi_calculadora (8, 4, "division")) 



