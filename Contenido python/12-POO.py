#Class 
class Auto:
    marca = ""
    modelo = 2001
    placa = ""
taxi = Auto()  # Taxi vendría a ser el objeto!! 
print(taxi.modelo)

# class y objetos II
class Persona:
    doctor = "Julieta"
#print(Persona.doctor)
#---------- Vamos con otro ejercicio
class Jugadores_A:
    j1 = "messi"
    j2 = "c.ronaldo"
    j3 = "Neymar" # Las J serían objetos mientras que los nombres de las j son los valores de esos objetos
print(Jugadores_A.j2) 

class Jugadores_B:
    j4 = "maradona"
    j1 = "Depaul"

print (Jugadores_B.j1) 

# Vamos a crear otra clase :
class nombre:
    pass 

victor = nombre() 
maria = nombre()

#objeto.atributo = valor 

victor.edad = 30 
victor.sexo = "Masculino"
victor.pais = "Argentina"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Brasil"

print (victor.edad)
print (maria.pais) 

# Metodos: un metodo es una funcion que se encuentra dentro de una clase  (determina una acción o un comportamiento)
class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 4
s = Matematica()
s.suma()
print(s.n1 + s.n2)
































