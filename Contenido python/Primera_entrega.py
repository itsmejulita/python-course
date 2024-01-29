def registro (user, password): 
# Acá creamos un diccionario vacío para almacenar el nombre de usuario y la contraseña.
    credencial = {}
# Acá se guarda el usuario y la contraseña del dicionario.   
    credencial[user] = password 
    return credencial 

def leer_datos (registro): 
    for user in registro.keys(): 
        print ("user:", user) 

# Ahora voy crear una función para loguearme 
def login (user, password, credencial):
    # Verica si el usuario existe en el diccionario 
    if user in credencial:  
        password_save = credencial[user]  
        if password == password_save: 
            print ("Iniciaste sesión.") 
        else: 
            print ("Contraseña incorrecta.") 
    else: 
        print ("No existe el usuario.") 



new_user = registro ("juliana", "estrella123")
leer_datos (new_user) 

login ("juliana", "estrella123", new_user) 












