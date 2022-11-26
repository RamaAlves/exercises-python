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

""" class Persona:
    #atributos
    def __init__(self,nombre,edad,genero,estatura,peso):
        self.__nombre=nombre
        self.edad=edad
        self._genero=genero
        self.estatura=estatura
        self.peso=peso
    
    #metodos
    def hablar(self):
        print(f"Hola soy {self.__nombre}")
    def correr(self):
        print(f"{self.__nombre} esta corriendo")
    def caminar(self):
        print(f"{self.__nombre} esta caminando")

#instanciacion
persona1 = Persona("Juan", 45, "Masculino", 170, 80)
persona2 = Persona("Julia", 25, "Femenino", 160, 58)

print(type(persona1))
print(persona1.__nombre)
print(persona1.edad)
print(persona1._genero)
print(persona1.estatura)
print(persona1.peso)
persona1.hablar()
persona1.correr()
persona1.caminar()



print(type(persona2))
print(persona2.__nombre)
print(persona2.edad)
print(persona2._genero)
print(persona2.estatura)
print(persona2.peso)
persona2.hablar()
persona2.correr()
persona2.caminar()

#ver tipos de datos
print(Persona.__name__)
print(type(persona1).__name__)
print(persona1.__class__.__name__)
 """

""" class Fecha():
    def __init__(self) -> None:
        self.__dia=1
    
    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia>0 and dia<=31:
            self.__dia= dia
        else:
            print("Error")
    
mi_fecha = Fecha()
#print(mi_fecha.__dia) # no puedo acceder a un atributo privado desde afuera
mi_fecha.setDia(33) #la unica forma de modificar el atributo de mi clase es por medio del metodo
#mi_fecha.__dia=30 #no puedo acceder desde afuera
mi_fecha.setDia(30) #la unica forma de modificar el atributo de mi clase es por medio del metodo
print(mi_fecha.getDia()) """

#Herencia

""" class Instrumento:
    def __init__(self, precio):
        self.precio=precio
    def tocar(self):
        print("estamos tocando musica")
    def precio_total(self):
        print(self.precio*1.21)

class Bateria(Instrumento):
    pass

class Bajo(Instrumento):
    def __init__(self, precio, tipo_cuerda):
        Instrumento.__init__(self, precio)
        self.tipo_cuerda=tipo_cuerda

bajo1 =Bajo(100, "steel")

print(bajo1.tipo_cuerda)
bajo1.precio_total() """

#herencia multiple

""" class Terrestre:
    def __init__(self) -> None:
        pass
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self) -> None:
        pass
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    def __init__(self) -> None:
        super().__init__()
c=Cocodrilo()
c.desplazar()

class Terrestre:
    def __init__(self) -> None:
        print("Este es el constructor de terreste")
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self) -> None:
        print("Este es el constructor de acuatico")
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    def __init__(self) -> None:
        super().__init__() """

#Herencia multinivel

""" class Figura:
    def __init__(self,area) -> None:
        self.area=area
    def retornar_area(self):
        print ("el area es ", self.area)
    
class Poligono(Figura):
    def __init__(self, area, lados) -> None:
        super().__init__(area)
        self.lados=lados
    def retornar_lados(self):
        print ("Los lados del poligono son ", self.lados)
    
class Cuadrilatero(Poligono):
    def __init__(self, area, lados) -> None:
        super().__init__(area, lados)

cudrado = Cuadrilatero(20,4)
cudrado.retornar_area()
cudrado.retornar_lados() """

#
""" print(Cuadrilatero) """


#polimorfismo
#sobrecarga de metodos

""" class Persona:
    def __init__(self,cedula):
        self.cedula=cedula
    def mensaje(self):
        print("mensaje desde la clase persona")

class Obrero(Persona):
    def __init__(self, cedula):
        super().__init__(self, cedula)
        self.__especialista= 1
    def mensaje(self):
        print("mensaje de obrero")

persona1=Persona(6)
obrero1=Obrero(2)
persona1.mensaje()
obrero1.mensaje() """





#ejercicios
#1
""" class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color= color
        self.__ruedas= ruedas
    
    def __str__(self):
        return f"color y ruedas en mi vehiculo: {self.__color, self.__ruedas}"
    
    def get_color(self):
        return self.__color
    
    def get_ruedas(self):
        return self.__ruedas

    def set_color(self, nuevoColor):
        self.__color = nuevoColor
    
    def set_ruedas(self, nuevasRuedas):
        self.__ruedas = nuevasRuedas
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color,ruedas)
        self.__velocidad= velocidad
        self.__cilindrada= cilindrada
    
    def __str__(self):
        return f"{super().__str__()}, velocidad y cilindrada: {self.__velocidad, self.__cilindrada}"
    
    def get_velocidad(self):
        return self.__velocidad
    
    def get_cilindrada(self):
        return self.__cilindrada

    def set_velocidad(self, nuevaVelocidad):
        self.__velocidad = nuevaVelocidad
    
    def set_cilindrada(self, nuevaCilindrada):
        self.__cilindrada = nuevaCilindrada
    
coche1 = Coche("rojo", 4, 120, 2000)
print("creando coche")
print(coche1)
print(coche1.get_ruedas())
print(coche1.get_color())
print(coche1.get_velocidad())
print(coche1.get_cilindrada())
print("modificando valores de coche")
coche1.set_color("azul")
coche1.set_ruedas(5)
coche1.set_velocidad(150)
coche1.set_cilindrada(1800)
print("mostrando datos modificados del coche")
print(coche1)
print(coche1.get_ruedas())
print(coche1.get_color())
print(coche1.get_velocidad())
print(coche1.get_cilindrada())
 """

#1
""" class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color=color
        self.__ruedas=ruedas
    
    def __str__(self):
        return f"color y ruedas: {self.__color, self.__ruedas}"
    
    def get_ruedas(self):
        return self.__ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.__velocidad=velocidad
        self.__cilindrada=cilindrada
    
    def __str__(self):
        return f"{super().__str__()}, velocidad y cilindrada: {self.__velocidad, self.__cilindrada}"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.__carga= carga
    
    def __str__(self):
        return f"{super().__str__()}, carga: {self.__carga}"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo=tipo

    def __str__(self):
        return f"{super().__str__()}, tipo: {self.__tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.__velocidad=velocidad
        self.__cilindrada=cilindrada
    
    def __str__(self):
        return f"{super().__str__()}, velocidad y cilindrada: {self.__velocidad, self.__cilindrada}"

moto= Motocicleta("rojo",2,"deportiva",300,1000)
bici= Bicicleta("azul", 2, "mountain-bike")
camioneta= Camioneta("verde",4,180,2000,1000)
coche=Coche("negro",4,200,2000)

lista_vehiculos=[moto,bici,camioneta,coche]

#def catalogar(lista_vehiculos):
#    for vehiculo in lista_vehiculos:
#        print(vehiculo.__class__.__name__)
#        print(vehiculo)

def catalogar(lista_vehiculos, ruedas=None):
    if ruedas !=None:
        contador =0
        for vehiculo in lista_vehiculos:
            if vehiculo.get_ruedas()==ruedas:
                contador+=1
                print(vehiculo.__class__.__name__)
                print(vehiculo)
        print(f"se han encontrado {contador} vehiculos con {ruedas} ruedas")
        return
    for vehiculo in lista_vehiculos:
        print(vehiculo.__class__.__name__)
        print(vehiculo)

print("mostrando lista completa")
catalogar(lista_vehiculos)
print("lista de vehiculos con dos ruedas")
catalogar(lista_vehiculos,2)
print("lista de vehiculos con cuatro ruedas")
catalogar(lista_vehiculos,4) """

#3
class Triangulo:
    def __init__(self, l1, l2, l3):
        self.__l1=l1
        self.__l2=l2
        self.__l3=l3
    
    def get_lado_mayor(self):
        if self.__l1>self.__l2 and self.__l1>self.__l3:
            return self.__l1
        else:
            if self.__l2>self.__l3:
                return self.__l2
            else:
                return self.__l3
    
    def tipo(self):
        if self.__l1== self.__l2 and self.__l1== self.__l3:
            return "equilátero"
        elif self.__l1== self.__l2 or self.__l1== self.__l3 or self.__l2== self.__l3:
            return "isóceles"
        else:
            return "escaleno"

triangulo1 = Triangulo(2,2,2)
triangulo3 = Triangulo(2,2,3)
triangulo2 = Triangulo(2,3,4)

print(triangulo1.get_lado_mayor())
print(triangulo1.tipo())
print(triangulo2.get_lado_mayor())
print(triangulo2.tipo())
print(triangulo3.get_lado_mayor())
print(triangulo3.tipo())