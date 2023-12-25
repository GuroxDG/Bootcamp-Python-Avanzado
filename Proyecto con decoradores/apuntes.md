# Refuerzo

* Link: https://towardsdatascience.com/python-decorators-a-comprehensive-guide-5bde06d2fb27
* Link: https://towardsdatascience.com/decorating-methods-defined-in-a-class-with-python-4b361589440

# Temas
* Patrones de diseño
* Clasificación de los patrones de diseño
* Patrón Decorator
* Proyecto

# ¿Qué son los patrones de diseño?

Los patrones de diseño son soluciones habituales a problemas que ocurren con frecuencia en el diseño de software. Son como planos prefabricados que se pueden personalizar para resolver un problema de diseño recurrente en tu código

# Clasificación de los patrones de diseño

## Patrones Creacionales

Proporcionan varios mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización de código existente.

* Factory Method: Proporciona una interfaz para la creación de objetos en una superclase, mientras permite a la subclases alterar el tipo de objetos que se crearán.(pruebas unitarias para simular comportamiento de clases)
* Abstract Factory: Permite producir familias de objetos relacionados sin especificar sus clases concretas.
* Builder: Permite construir objetos complejos paso a paso. Este patron nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
* Prototype: Permite copiar objetos existentes sin que el código dependa de sus clases.
* Singletton: Permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a la dicha instancia.(Instancias en bases de datos en desarrollo web) 

## Patrones Estructurales

Explican cómo ensamblar objetos y clase en estructuras más grandes, a la vez que se mantiene la flexibilidad y eficiencia de estas estructuras.

* Adapter: Permite la colaboración entre objetos con interfaces incompatibles.
* Bridge: Permite dividir una clase grande o un grupo de clases estrechamente relacionadas, en dos jerarquías separadas(abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.
* Composite: Permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.
* Decorator: Permite añadir funcionalidades a objetos colocando estos obejtos dentro de objetos encapsuladores especiales que contienen estas funciones.
* Facade: Proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.
* Flyweight: Permite mantener más objetos dentro de la cantidad disponible de memoria RAM compartiendo las partes comunes del estado entre varios ibjetos en lugar de mantener toda la información en cada objeto.
* Proxy: Permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

## Patrones de Comportamiento

Tratan con algoritmos y la asignación de responsabilidades entre objetos.

* Chain of Responsibility:
* Command:
* Iterator:
* Mediator:
* Memento:
* Observer:
* State:
* Strategy:
* Template Method:
* Visitor:


# Patrón Decorator

Es un patron de diseño estructural que te permite añadir funcinalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

Ejemplos de un proyecto con decoradores usando clases en Python:

* Logging: Un decorador puede ser usado para añdir funcionalidad a un clase. Esto puede ser util para trazar la ejecución de unos métodos de clase.
* Autenticación: Un decorador puede ser usado para añadir funcionalidad de autenticación a una clase. Esto puede ser usasdo para restringir el acceso a métodos de clase a usuarios autorizados.
* Caching: Un decorador puede ser usado para añadir funcionalidad de cacheo a una clase. Esto puede ser usado para mejorar el performance de una clase almacenando los resultados de operaciones computacionales costosas en memoria.
* Rate limiting: Un decorador puede ser usado para añadir funcionalidad de rate limiting a una clase. Esto puede ser usado para prevenir que una clase sea sobrecargada con request