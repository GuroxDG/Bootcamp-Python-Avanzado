# Temas 
* Módulos
* Importación
* Paquetes
* init & main
* setup.py

# Módulos
Es un fichero .py que contiene definicioens de variables, funciones y clases que pueden ser reutilizadas por otros programas

Tips para nombrarlos:
* Usar minúsculas
* Usar snake_case
* Ser descriptivos
* Evitar nombres muy genéricos

¿Para qué sirven las variables?

if __name__ == "__main__":
    [bloque de código]

# Importación de Módulos

* import [nombre_módulo]
* from [nombre_módulo] import [nombre_método]
* import [nombre_módulo] as [alias_módulo]
* hay que evitar la recursión en la importación de modulos
* No más de 100 líneas en una función

documentación:
* https://docs.python.org/es/3/tutorial/modules.html
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* setuptools pype

# Paquetes 

Un paquete es un directorio que contiene uno o más módulos permitiendo una organización jerárquica entre ellos

```
modulo_matematica/
    | -- __init__.py
    | -- arimetica.py
    | -- geometria.py
```

# setup.py

Es un archivo de configuración utilizado en proyectos de Python que se distribuyen como paquetes

```
from distutils.core import setup

setup(name='Distutils',
    version = '1.0',
    description = 'Python Distribution Utilities',
    author = 'Greg Ward',
    author_email = 'qward@python.net',
    url = 'https://www.python.org/sigs/distutils.sig/',
    packages = ['distutils', 'distutils.command'],   
)
```

crear paquetes distribuibles para instalarlos al ambiente global de Python
py setup.py sdist
