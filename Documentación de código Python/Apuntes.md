# Temas
1. Intro
2. Comentar vs Documentar: Docstring, type, hints y help()
3. Documente y pruebe su código a la vez: Módulo Doctest
4. Documentación Auto generada: reStructuresText y Sphinx
5. Estrategias para documentar proyectos
6. Extras:
    * Proyectos Open Source
    * Documentando APIs con Swagger

# Documentación
Tiene como objetivo explicar como funciona el código o cómo usarlo dependiendo de para quién está escrito (usuarios o desarrolladores)

* Comentar es describir su código para otros desarrolladores y/o mantenedores del código
* Documentar código es describir su uso y funcionalidad a sus usuarios

## Comentarios
Se considera un subconjunto de la documentación, ayudan a:
* Entender código
* Hacer que se explique por si mismo
* Entender su propósito y diseño

# Docstrings
Son cadenas integradas en nuestra funciones, métodos, clases, módulos o paquetes, que nos ayudan a la documentación
* La primera línea debe dar una descripción
* Se prefieren comillas dobles
* Se acceden mediante el atributo ____doc____
* La segunda línea deberá ser un espacio en blanco

# Función Help()
Proporciona a los programadores la documentación asociada a un objeto
help('collections')

# Docstring en paquetes 
En el caso de los paquetes el docstring debemos establecerlo en la primera línea del iniciador: __init__.py

```
Help on pakage calculator

NAME
    calculator # package

PACKAGE CONTENTS 
    calculations
    figures
    statistics

FILE
    ruta:c//

```

# Formatos soportados de Docstring

|__Formatting Type__|__Description__|__Supported by Sphynx__|__Formal Specification__|
|----|------|--|--|
|Google docstrings|Google's recommended form of documentation|Yes|No|
|reStructuredText|Official Python documentation standar|Yes|Yes|
|Numpy/Scipy docstring|Numpy's comination of reStructuredText and Google docstrings|Yes|Yes|
|Epytext|A Python adaptation of Epydoc|Not Officially|Yes|

## Estilo Google
```
"""
This is an example of Google style

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a dexcription of what is returned

Raises:
    KeyError: Raises an exception
"""

```

## Estilo reStructuredText
```

"""
This is a reST style.

:param param1: This is the first param.
:param param2: This is a second param.

:returns: This is a dexcription of what is returned

:raises: KeyError: Raises an exception

"""
```


## Estilo Numpy/Scipy
```"""This is a reST style.

Parameters
----------
param1 : str
    This is the first param.
param2 : str
    This is a second param.

Returns
-------
This is a dexcription of what is returned
"""
```

## Estilo Epytext
```
"""
This is a reST style.

@param param1: This is the first param.
@param param2: This is a second param.
@returns: This is a dexcription of what is returned
@raises: KeyError: Raises an exception

"""
```

# Type Hints o anotations

Son anotaciones para agregar tipos a variables, etc..., son solo sugerencias
```
<variable_name>: <variable_type> = <variable_value>
```

