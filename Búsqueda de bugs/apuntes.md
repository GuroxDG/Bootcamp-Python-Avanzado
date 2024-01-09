# Temas 

* Excepciones
* Traceback
* Módulo Logging
* Archivo de logs
* Módulo doctest
* Módulo dbp
* Type Hints & Anotaciones

# ¿Cómo evitar crear bugs?

* No escribir código 😊

# ¿Cómo encontrar bugs?

* Mantén todo simple
* Sigue los entandares de tu equipo de desarrollo y de la comunidad
* Los errores no deben pasar en silencio
* Documenta tu código
* No es necesario re-inventar la rueda.

# Excepción
Mecanismo que se activa con forme a un error en tiempo de ejecución.

Las excepciones heredan de  __BaseException__

## Más vale pedir perdón que pedir permiso.

* En Python, al ocurrir un error en tiempo de ejecución se dispara una excepción, lo que finaliza el programa de forma abrupta.
* Las excepciones las manejaremos con los bloques: try - except

# Traceback

* En Python, el Traceback (rastro de ejecución) es una lista de llamadas y excepciones que se muestra cuando ocurre un error.
* Proporciona información detallada sobre la secuencia de eventos que condujo al error
* Es posible extraer el traceback aunque python lo omita con el exception

# Módulo Logging

__Deja de usar prints__
```
def my_super_function(*args):
    print(">>>> Entramos a al función")
    ...
    print(">>>> Salimos de la función")
    return True
```

logging trabaja con 6 niveles de categorías

```
import logging

logging.debug("Este es un mensaje debug")
logging.info("Este es un mensaje de información")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje critico")
```
por defecto en python se imprime todo lo qu eeste por encima del nivel 30 (30, 40, 50)

## Configuración de logging

```
logging.basicConfig(
    filename="basic.log",
    encoding="utf-8",
    level=logging.INFO,
    filemode = "W",
    format = "%(process)d-%(levelname)s-%(message)s"
)
```

## Formato de mensajes

* $(asctime)s: La hora en la se registra el mensaje
* $(levelname)s: El nivel de registra del mensaje
* $(message)s: El contenido del mensaje
* $(name)s: El nombre del logger utilizado
* $(filename)s: El nombre del archivo donde se realiza el registro
* $(module)s: El nombre del modulo donde se realiza el registro
* $(funcName)s: El nombre de la función donde se realiza el registro
* $(lineno)d: El número de la línea donde se realiza el registro

# Módulo pdb

>>> import pdb
>>> breakpoint()

* __n o next:__ Ejecuta la siguiente línea de código
* __s o step:__ Entra en la siguiente función llamada
* __c o continue:__ Continúa la ejecución hasta el próximo punto de interrupción
* __l o list:__ Muestra el fragmento de código actualmente en ejecución
* __p <variable>:__ Muestra el valor de una variable
* __q o quit:__ Sale del modo de depuración y finaliza el programa:

