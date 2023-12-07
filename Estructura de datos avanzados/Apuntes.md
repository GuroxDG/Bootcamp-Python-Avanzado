# Temas

* Estructura de datos
    - Lists
    - Dicts
    - Sets
* Iteradores
* Generadores
* Iterables
* Corrutinas   

# Estructura de datos

## Listas y Tuplas

### Listas
Características:
* Están ordenadas
* Pueden contener cuaquier objeto arbitrario
* Se puede acceder a los elementos de la lista por índice
* Se pueden anidar a una profundidad arbitraria
* Las listas son mutables
* Las listas son dinámicas

### Tuplas
Igual a las listas excepto en:
* Se definen encerrando los elementos entre paréntesis en de corchetes
* Las tuplas son inmutables

### Iterar sobre una lista
Usando 
* For Loop
* map()
* filter()
* List Comprenhensions
    - filter_list = [expression for member in iterable __(if conditional)__]
    - modify_list = [expression __(if conditional)__ for member in iterable]

## Dicts

Colección de pares clave-valor (key-value)
* mutables
* dinámicos
* No son ordenados
* Los diccionarios solo reciben keys inmutables

## Sets

Características
* Estan desordenados
* los elementos son únicos, no se permite elementos duplicados
* Un conjunto en si puede modificarse, pero los elementos contenidos en el conjunto deben ser de tipo inmutable
* {} or set([])

# Iteradores e iterables

Los iteradores potencian y controlan el proceso de iteración, mientra que los iterables normalmente contienen datos que desean iterar sonre un valor a la vez


## Iteradores
Los iteradores de Python, implementan el pratron de diseño Iterador, que le permite recorrer una colección y acceder a sus elementos


## Protocolo Iterador
Estos dos métodos hacen que los iteradores de Python funcionen, Por lo tanto, si desea crear clases iteradoras personalizadas, debe implementar los siguientes métodos:

| __Method__ | __Description__ |
|--|----|
|.____iter__()|Llamado para incializar el iterador. Debe devolver un objeto iterador|
|.____next__()|Llamado para iterar sobre el iterador. Debe devolver el siguiente valor en el flujo de datos|

# Generators
Tipos especiales de iteradores que permiten crearlos como función
* Generator Expressions ([])