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


```
external_variable = ["Hola", "Mundo"]

def remove_last_value():
    external_variable.pop()

print(external_variable)
# ['Hola', 'mundo']

remove_last_value()

print(external_variable)
# ['Hola']
```

# Funciones como ciudadanos de primer orden
Se refieren a elementos en un lenguaje de programación que pueden ser tratados de manera completa y sin restricciones

Estos elementos pueden ser asignados a variables, almacenados en estructuras de datos, pasados como argumentos a funciones y devueltos como resultados de funciones

```
def my_function():
    print('I am function my_function()')    
```

Ser asignados a variables
```
my_function()
# I am function my_function()

another_name =  my_function
another_name()
# I am function my_function()
```

Almacenados en estructuras de datos
```
objects = ['cat', my_function, 42]
print(objects[1])
# <function>

dictionary = { 'cat': 1, my_function : 2, 42 : 3 }
print(dictionary[my_function])
# 2
```

Pasados como argumento a funciones
```
def inner():
    print('I am function inner()')

def outer(function_param):
    function_param()

outer(inner)
# I am function inner()
```

Devueltos como resultado de funciones
```
def outer():
    def inner():
        print('I am function inner()')
    return inner

returned_function = outer()
returned_function()
#'I am function inner()'

print(returned_function)
# <function outer.<local>.inner >
```

# Función de orden superior

Se denomina de orden superior si esta contiene otras funciones como parámetros de entrada o si devuelve una función como salida, es decir, las funciones que operan con otra función se conocen como funciones de orden superior en Python.

```
def inner():
    print('I am a function called by a high order')

def high_order_function(function_param):
    function_param()

high_order_function(inner)
```

## Filter como función de orden superior

```
def get_even(x):
    return x%2 == 0

integer = range(100)
even = list(filter(get_even, integer))
print(even)
# [0, 2, 4, 8, ..., 98]
```

# Funciones recursivas

Una función recursiva es una función que se define en términos de sí misma a través de una expresión autorreferencial. Eso significa que la función se llama a sí misma y repite el comportamiento hasta que se cumple alguna condición, y luego devolverá un resultado.

Básicamente la recursividad permite diseñar algoritmos que de forma iterativa generarían más código y serían menos legibles.

```
def countdown(n):
    print(n)
    if n > 0:
        countdown(n-1)

countdown(5)
# 5
# 4
# 3
# 2
# 1
# 0
```

# Funciones lambda

Las funciones lambda son funciones anónimas que solo pueden contener una expresión

__lambda <parameter_list>:<_expression_>__

Component | Meaning
---|----
_lambda_ | Palabra clave para definir una expresión lambda
_<parameter_list>_ | Una lista de nombres de parámetros opcionales
_:_ | Puntuación para separar los parámetros de la expresión
_<_expression_>_ | Una expresión que normalmente incluye los parámetros

```
def get_even(x):
    return x%2 == 0

get_even
# <function get_even at ...>

lambda x : x%2 == 0
# <function <lambda> at ...>
```

Una función lambda es callable (llamable o invocable)

```
callable(lambda s: s[::-1])
# True
```

Una función lambda es asignable a variables
```
def reverse(s):
    return s[::-1]

reverse('I am a string')
# gnirts a ma I

lambda_reverse = lamda s : s[::-1]
lambda_reverse('I am also a string')
# gnirts a osla ma I
```

Una función lambda puede se llamada inmediatamente (IIFE)
```
(lamda s: s[::-1])('I am a string')
# gnirts a ma I
```

Una función lambda puede recibir multiples parámetros
```
lambda_average = lambda x1, x2, x3: (x1 + x2 + x3) / 3
lambda_average(3, 6, 9)
# 6.0
```

Una función lambda puede no recibir parámetros
```
meaning_of_life = lambda: 42
meaning_of_life()
# 42
```

Una función lambda pueden retornar múltiples resultados en una tupla pero solo de forma explicita
```
def my_function(x):
    return x, x ** 2, x ** 3

my_function(3)
# (3, 9, 27)
```

Error al no denifir la tupla función
```
(lambda x: x, x ** 2, x ** 3)(3)
# Traceback (most recent call last):
# NameError: name 'x' is not defined

(lambda x: (x, x ** 2, x ** 3))(3)
# (3, 9, 27)
```

Una función lambda puede retornar una lista o un diccionario
```
(lamda x: [x, x ** 2, x *** 3])(3)

(lamda x: {1:x, 2:x ** 2, 3:x *** 3})(3)
```

Una función lambda puede ser creada dentro de un f-string pero debe ser encerrada dentro de paréntesis

```
print(f"--- {lambda s: s[::-1]} ---")
# SyntaxError: f-string invalid syntax

print(f"--- {(lambda s: s[::-1])} ---")
# --- <function <lambda> at ...>

print(f"--- {(lambda s: s[::-1])('I am a string')} ---")
# --- gnirts a ma I ---
```