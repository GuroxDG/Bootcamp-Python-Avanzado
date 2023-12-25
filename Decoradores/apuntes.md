# Decoradores

Son un patron de diseño en Python que permite agregar funcionalidades a un objeto existente (funciones o clases) sin modificar su estructura

```
@example_decorador
def test_function():
    return 'output'
```

# Como trabajan las funciones

Funciones retornan un valor de acuerdo al argumento que le pasamos

Funciones como parámetros

```
def plus_one(number):
    return number + 1

as_funciton = plus_one
as_function(5)
```

Funciones dentro de funciones (Closures)

```
def plus_one(number):
    def add_one(number):
        print('Executting add_one')
        return number + 1
    
    print('Executting plus_one')
    result = add_one(number)
    return result

plus_one(4)
```

Funciones como argumentos de otras funciones

```
def plus_one(number):
    print('Executting plus_one')
    return number + 1

def function_call(function):
    print('Executting function call')
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
```

Funcipon puede retornar otra función

```
def hello_function():
    def say_hi():
        print('Executtting say_hi')
        return 'Hi'
    print('Executtinh hello_function')
    return say_hi

hello = hello_function()
hello()
```

Las funciones anidadas tienen acceso a las variables de la funcion envolvente

```{python}
def print_message(message):
    """Enclosing Function"""

    def message_sender():
        """Nested Function"""

        print(message)
    
    message_sender()

print_message('Some random message')
```

## Características
* Un decorador tiene una funcipon anidada generalmente conocida como wrapper
* Según PEP8 máximo se pueden anidar 2 niveles
* Se usa decoradores en vez de usar llamada de función que recibe como parámetro otra función debido a temas de legibilidad
* Un decorador puede agregar la funcionalidad que uno requiera
* El orden de ejecución en una función con dos decoradores depende del nivel de cercanial de @decorador
* Los decoradores son un patron de diseño
* se guarda decoradores en un archiv o decoradores.py

# Args y Kwargs

* *args: es usado para recibir múltioles argumentos por posición.
* **kwargs: es usado para recibir múltioles argumentos por medio de una llave o key.

```
def test_args_and_kwars(*args, **kwargs):
    print('args')
    for arg in args:
        print(f'arguments of arg: {arg}')
    print('kwargs')        
    for key, value in kwargs:
        print(f'{key} = {value}')
```

* links : http://www.freecodecamp.org/espanol/news/los-principios-solid-explicados-en-espanol
* pdb Python debugger