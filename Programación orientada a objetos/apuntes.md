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

