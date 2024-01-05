# Temas 
* ¿Qué es POO?
* Clases y objetos
* Herencia 
* Polimorfismo
* Encapsulamiento
* Abstracción

# ¿Qué es POO?

La programación orientada a objetos es un paradigma de programación que parte del concepto de "objetos" como base, los cuales contienen información en forma de campos (a veces también referidos como atributos o propiedades) y código en forma de métodos.

Los objetos son capaces de interactuar y modificar los valores contenidos en sus campos o atributos (estado) a través de sus métodos (comportamiento)

Una clase es una especie de "plantilla" en la que se definen los atributos y métodos predeterminados de un tipo de objeto. Esta plantilla se crea para poder crear objetos fácilmente

```
class ClassName:
    pass
```

Un objeto es una instancia de una clase.

```
new_obj = ClassName()
```

# Herencia

La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos

```
class ChildClass(FatherClass):
    pass
```

En python es posible realizar hrencia múltiple. La herencia múltiple consiste en que una clase herreda de varias clases padre en vez de una sola al mismo tiempo.
Exite un orden de herencia de izquierda a derecha.

```
class Class1:
    pass
class Class2:
    pass
class Class3(Class1, Class2):
    pass
```

# Polimorfismo

El término tiene origen en las palabras poly(muchos) y morfo(formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas

```
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Guau!")

class Cat(Animal):
    def speak(self):
        print("Miau!")
```

# Encapsulamiento

Consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.

```
class Base:
    class_attribute = "Hi"
    __hidden_class_attribute = "Pribate Hi"

    # No accesible desde el exterior
    def __private_method(self):
        print("Do Somethig")
        self.__variable = 0

    # Accesible desde el exterior
    def public_method(self):
        self.__private_method()
```
link: https://realpython.com/inheritance-composition-python/

# Abstracción

Es un término que hace referencia a la ocultación de la complejidad intrínsica de una aplicación al exterior,  centrándose sólo en cómo puede ser usada, lo que se conoce como interfaz.

Un concepto relacionado con la abtracción, serían las clases abtractas o más bien los métodos abtractos, y se define como método abtracto a un método que ha sido declarado pero no implementado, Es decir, que no tiene código.

En python usamos el módulo ABC (Abstrac Base Classes) para implementar interfaces formales

```
from abc import ABC

class RemoteControl(ABC):
    pass

from abc import ABCMeta

class RemoteControl(metaclass=ABCMeta):
    pass
```

En la abstracción debemos decir cuales métodos son abstractos, todos los métodos abstractos tienen que definidos el los objetos que heredan del abstract


# Tema 2

* Magic Methods
* Miembros públicos, protegidos y privados
* Name Mangling
* Properties
* Metodos de instancia, clase y estáticos
* Data Classes


# Magic Methods

Los métodos mágicos o dunder functions son un conjunto de métodos predefinidos en python que nos proveen funcionalidades sintácticas especiales. Estos nos permiten que los objetos propios se comporten similar a los tipos incorporados de Python. Se puden reconocer fácilmente porque inician y terminan con dos guiones bajos, por ejemplo __init__, __cal__ y __len__

link : https://rszalski.github.io/magicmethods/

# Miembros públicos, protegidos y privados

__Miembros Públicos:__ Pueden ser accedidos desde afuera de la clase. Todos los miembros de una clase en Python son públicos por defecto.

__Miembros Protegidos:__ Son accedidos desde la clase en donde son definidos o subclases que los heredan.

__Miembros Privados:__ Su uso no es restringido pero sugiere que no se deben manipular por fuera de la clase.

```
class ClassName:
    public_attribute = "Hi I'm Public"
    _protected_attribute = "Hi I'm Protected"
    __private_attribute = "Hi I'm Privated"
```


# Properties

Los Properties son la forma pythonica de evitar la creación de métodos para obtener y modificar atributos de una clase.

Esta función nos ayuda a convertir atributos de una clase en properties o managed attributtes.

```
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property"""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("delete radius")
        del self._radius
```

# Métodos de instancia, clase y estáticos

__Métodos de instancia:__ son creados para modificar un objeto instanciado de una clase.

__Métodos de clase:__ trabajan directamente con la clase, desde que su parámetro es la clase en sí.

__Métodos estáticos:__ no saben nada acerca de la clase, solo trabajan con los parámetros recibidos.

```
class MyClass:
    # Ejemplo método de instancia
    def method(self):
        return "instance method called", self

    # Ejemplo método de clase
    @classmethod
    def class_method(cls):
        return "class method called", cls

    # Ejemplo método estático
    @staticmethod
    def static_method():
        return "static method called"
```

Resumen de métodos de instancia, clase y estáticos.
* Los métodos de instancia necesitan una instancia de una clase y puede acceder dicha instancia por medio de self
* Los métodos de clase no necesitan una instancia de una clase. Ellos no pueden acceder a la instancia(self), pero tienen acceso a la clase por medio de cls
* Los métodos estáticos no tienen acceso a cls o self. Ellos trabajan como funciones regulares pero pertenecen al namespace de la clase
* Los métodos estáticos y de clase son útiles al momento de diseñar una clase, estos tienen muchos beneficios en el mantenimeinto y lectura del código.

# Data Classes
Los data classes son una nueva forma de definir clases introducida en Python 3.7. Estos vienen con funcionalidades básicas que ya están implementadas ahorrandonos línes de código.

```
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float
```
