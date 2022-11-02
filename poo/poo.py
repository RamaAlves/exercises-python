""" paradigma: es el resultado de un proceso social en el cual un grupo de personas desarrolla nuevas ideas y crea principios y practicas alrededor de estas ideas """

""" en programacion se trata de un enfoque concreto de desarrollar y estructurar el desarrollo de programas """

""" paradigmas:

    imperativo
    declarativo
    funcional
    orientado a objetos """

""" orientacion a objetos:
    objeto ->  caracteristicas y cosas que puede hacer 
        
    clases: modelo que define las propiedades y comportamenientos de un objeto concreto. 
    abstracciones que representan a un conjunto de objetos con un comportamiento e interfaz comun"""

""" clase persona
    atributos:id, nombre, etc
    metodos:hablar(),correr(),etc. """

""" 
un objeto es una instancia de una clase por lo que se pueden intercambiar los terminos objeto o instancia """

""" caracteristicas: estado, comportamiento, identificador, """
""" los objetos solo existen en tiempo de ejecucion del programa, se instancian cuando se ejecuta el programa y se crean en memoria. 
no se almacenan en el disco """

class Persona:
    #atributos
    def __init__(self,nombre,edad,genero,estatura,peso):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.estatura=estatura
        self.peso=peso
    
    #metodos
    def hablar(self):
        print(f"Hola soy {self.nombre}")
    def correr(self):
        print(f"{self.nombre} esta corriendo")
    def caminar(self):
        print(f"{self.nombre} esta caminando")

#instanciacion
persona1 = Persona("Juan", 45, "Masculino", 170, 80)
persona2 = Persona("Julia", 25, "Femenino", 160, 58)

print(type(persona1))
print(persona1.nombre)
print(persona1.edad)
print(persona1.genero)
print(persona1.estatura)
print(persona1.peso)
persona1.hablar()
persona1.correr()
persona1.caminar()



print(type(persona2))
print(persona2.nombre)
print(persona2.edad)
print(persona2.genero)
print(persona2.estatura)
print(persona2.peso)
persona2.hablar()
persona2.correr()
persona2.caminar()

#ver tipos de datos
print(Persona.__name__)
print(type(persona1).__name__)
print(persona1.__class__.__name__)