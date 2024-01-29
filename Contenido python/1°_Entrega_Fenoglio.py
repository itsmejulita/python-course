# Crear un diccionario para almacenar los datos de los usuarios 
"""
usuarios = {}

# Funcion para registrar un usuario nuevo
def registrar_usuario (nombre, contraseña):
    usuarios [nombre] = contraseña

# Funcion para iniciar sesion 
def login (nombre, contraseña):
    if nombre in usuarios and usuarios in [nombre] == contraseña:
        return True
    else: 
        return False 
# Funcion para guardar los datos de los usuarios en un archivo txt
def guardar_datos():
    with open("usuarios.txt", "w") as f:
        for nombre, contraseña in usuarios.items():
            f.write(f"{nombre}:{contraseña}\n")
            
"""
###########################################################################
# BD = {}
# def user_password():
#     user = input("Ingrese su nombre de usuario!!: ")
#     f.write(user)
#     password = (input("Ingrese su contraseña: "))
#     f.write(password)

#     f.close()

# # Función para almacenar datos
# def almacenar_datos(user_password , BD):
#     if user in BD and BD [user] == password:
#     return True: 
#     else:
#     return False
#     BD[user] = [password, BD] 
#     return ("Datos almacenados") 

# def guardar_archivos(nombre_archivo, BD):
#     with open (nombre_archivo, "a") as archivo:
#     for user, password in BD.items():
#     archivo.write(f"{user}:{password}\n"):
# print(user_password)




bd = {}
def usuario_contraseña():
    user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    return (user, password)
    
    if user in bd:
    return ("El usuario ya existe!")

# Función para almacenar datos
def almacenar_datos(user_password , bd):
    if user in bd and bd [user] == password:
    return True
    else:
    return False
    BD[user] = [password, bd]
    return ("Datos almacenados")

def guardar_archivos(nombre_archivo, bd):
    with open (nombre_archivo, "a") as archivo:
    for user, password in bd.items():

    archivo.write(f"{user}:{password}\n")
# Guardar archivos txt
f = open(ruta+"/archivo.txt", "a")
datos = {}
with open ("archivo.txt", "a") as archivo:
    archivo.write:(datos) 
f.close()
print(usuario_contraseña)



    
