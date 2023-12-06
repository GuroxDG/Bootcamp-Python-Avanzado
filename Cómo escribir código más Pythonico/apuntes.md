# Preguntas Buenas Prácticas

* Forma correcta de escribir una función: __my_function__
* Forma correcta de escribir una constante: __MY_CONSTANT__
* Se debería usar espacios o tabs: __espacios__
* Nombrar una lista de nombre: __list_of_names__
* Forma de escribir una lista: __my_list = [1, 2, 3,]__
* Separación de términos: 
```
total = (first_variable
        + second_variable
        - third_variable)
```
* Se debe dejar una línea en blanco al final de los archivos en Python

# Naming Conventions
## Naming Styles

|__Type__|__Naming Convention__|__Examples__|
|----|------|---|
|Function|Use una palabra o palabras en minúsculas. separe las palabras con guiones bajos|__function__, __my_function__|
|Variable|Use una sola letra, palabra o palabras en minúsculas, separe las palabras con guiones bajos| __x__, __var__, __my_variable__|
|Class|Comienza cada palabra con una letra mayúscula, No use guiones use camel case o pascal case|__Model__, __MyClass__|
|Method|Use una palabra o palabras en minúsculas, separe las palabras con guiones bajos|__class_method__, __method__|
|Constant|Use una palabra o palabras en mayúsculas, separe las palabras con guiones bajos|__CONSTANT__, __MY_CONSTANT__|
|Module|Use una palabra o palabras cortas en minúsculas, separe las palabras con guiones bajos|__module__, __my_module__|
|Package|Use una palabra o palabras cortas en minúsculas, No separe las palabras con guiones bajos|__package__|

* La mejor manera de nombrar sus objetos en Python es __usar nombres descriptivos para dejar claro lo que representa el objeto__

# Code Layout
"Beautiful is better than ugly"

## Blank Lines

Los espacios en blanco verticales, o líneas en blanco, pueden mejorar en gran medida la legibilidad de su código.

* Rodee las funciones y clases de nivel superior con dos líneas en blanco.
* Rodee las definiciones de métodos dentro de las clases con una sola línea en blanco.
* Use líneas en blanco con moderación dentro de las funciones para mostrar pasos claros

## Maximun Line Length and Line Breaking

PEP 8 sugiere que las líneas deben limitarse a 79 carácteres.

# Identation

"Debería haber una sola forma que sobre salgo sobre las demas"

* Use 4 espacios consecutivos para indicar sangría
* Prefiere los espacios a los tabs

## Sangría despúes de los saltos de línea

mantener la sangría cuando se trate de la misma línea de código

## Dónde poner los cierres ?

Las continuaciones de línea le permiten romper líneas dentro de paréntesis, corchetes o llaves

# Comments

"Si la implementación es díficil de explicar, entonces es una mala idea"

## Dónde poner la abrazadera de cierre?

Puntos clave para recordar al agregar comentarios a su código:

* Limite la longitud de línea de los comentarios y la cadenas de documentación a 72 caracteres
* Usar oraciones completas, comenzando con una letra mayúscula
* Asegurate de actualizar los comentarios si cambias de código

# Whitespace in Expressions and Statements

"Sparse is better than dense"

## Espacios en blanco alrededor de los operadores binarios

Rodee los siguientes operadores binarios con un solo espacio a cada lado:

* Operadores de asignación (=, +=, -=, etc...)
* Comparaciones (==, !=, >, <, >=, <=) y (is, is not, in, not in)
* Booleanos (and, not, or)

## Cuándo evitar agregar espacios en blanco

La siguiente lsita describe algunos casos en los que debe evitar agregar espacios en blanco:

* Inmediatamente dentro del paréntesis, corchetes o llaves
* Antes de una coma, punto y coma o dos puntos
* Antes del paréntesis abierto que inicia la lista de argumentos de una llamada de función
* Antes del paréntesis abierto que inicia un índice o segmento
* Entre una coma final y un paréntesis de cierre
* Para alinear operadores de asignación

# Recomendaciones adicionales

" Simple es mejor que complejo"

* No compare valores booleanos ocno True o False usando el operador de equivalencia
* Utilice el hecho de que las secuencias vacías osn falsas en declaraciones if
* Use __is not__ preferiblemente sobre __not...is__ en declaraciones if
* No use __if x:__ cuando quiere decir __if x is not None:__
* Use __.startswith()__ y __.endswith()__ en lugar de usar recortar la palabra
