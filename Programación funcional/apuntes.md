# Temas

* Paradigmas de programación
* Programación funcional
* Python como lenguaje funcional
* Lambdas
* Maps y filters

# Paradigmas de la programación

Un paradigma de programación es un enfoque o conjunto de principios que guían la forma en que se estructura y se escribe el código en un lenguaje de programación.
Define la forma en que se modelan y se resuelven los problemas utilizando dicho lenguaje

## Programación Imperativa vs Declarativa

La programación imperativa describe qué pasos hay que dar para obtener la solución de un problema.
La programación declarativa se enfoca en describir qué/cuál es la solución sin entrar en detalles de su control se flujo.

### Imperativa
```
numbers = [18, 6, 4, 15, 55, 78, 12, 9, 8]

counter = 0
for number in numbers:
    if number > 10:
        counter += 1

print(counter)
# 5
```

### Declarativa
```
numbers = [18, 6, 4, 15, 55, 78, 12, 9, 8]

counter = len(list(filter(lambda num: num > 10, numbers)))

print(counter)
# 5
```

# Programación Funcional
La programación funcional es un paradigma de programación declarativo que se basa en el uso de funciones puras y evita el estado mutable y los efectos secundarios. Se centra en la evalución de expresiones y la composición de funciones para resolver problemas

El código funcional es:
* __Alto nivel__: está describiendo el resultado que desea en lugar de especificar explícitamente los pasos necesarios para llegar allí.
* __Transparente__: El comportamiento de una función pura depende únicamente de sus entradas y salidas, sin valores intermedios.
* __Paralelizable__: Las rutinas que no causan efectos secundarios pueden ejecutarse más fácilmente en paralelo entre sí.

# Python como lenguaje funcional
Python es un lenguaje de programación que admite múltiples paradigmas, lo que lo hace muy flexible y versátil.

Python tiene características de programación funcional ya que permite el uso de funciones de primera clase, funciones de orden superior, expresiones lambda y operaciones de lista (como map, filter y reduce) para realizar operaciones funcionales.

## Funciones Puras
* Devuelven el mismo resultado al ser llamadas con los mismos argumentos de entrada.
* El resultado solo depende de la entrada: no tienen memoria.
* No tiene efectos colaterales (side effects)

Dada una entrada siempre se espera la misma salida sin afectar valires externos o requerir de otras variables

```
def multiply_by_2(x):
    return x * 2

multiply_by_2(3) # 6
multiply_by_2(3) # 6
multiply_by_2(3) # 6
```
## Función Impura

Dado una entrada no se puede determinar la salida

```
from random import randint

def multiply(x):
    return x * randint(1, 10)

multiply(3) # 3
multiply(3) # 15
multiply(3) # 27
```

Su resultado depende de variables externas

```
external_variable = ["Hola", "Mundo"]

def custom_join():
    new_string = ""
    for word in external_variable:
        new_string += word
    return new_string

custom_join()
# Holamundo
```

Su ejecución genera efectos secundarios modificando el estado de otras variables
