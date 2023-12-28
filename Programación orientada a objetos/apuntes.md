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

