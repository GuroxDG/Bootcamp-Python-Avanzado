# Temas

* Pruebas automátizadas
* Desarrollo guiado por pruebas (TDD)
* Pytest
* Coverage 


# Pruebas automátizadas

validan que el software funciona según lo previsto antes de pasar a producción, entre sus ventajas están:
* Detección temprana de errores
* Ahorro de tiempo y esfuerzo a largo plazo
* Mayor confianza en el código
* Facilita la colaboración en equipos
* Mejora la calidad de software

## Piramide de pruebas

Es un concepto utilizado en el desarrollo de software para representar la distribución y proporción ideal de diferentes tipos de pruebas automátizadas. 

La Piramide de pruebas consta de tres capas principales, desde la base hasta la cúspide:
1. Pruebas unitarias
2. Pruebas de integración
3. Pruebas de interfaz de usuario(UI)

```
           - GUI - 
        -- API Test --
    --- Integration Test ---
    ---- Component Test ----
     ----- Unit Test -----
```

## Pruebas unitarias

La base de la Piramide está compuesta por las pruebas unitarias. Estas pruebas se centran en verificar el comportamiento individual de unidades de código aisladas, como funciones, métodos o clases- Se suelen escribir utilizando frameworks específicos de pruebas unitarias y son rápidas de ejecutar.

La pruebas unitarias proporcionan una cobertura exahustiva de los componentes de bajo nivel y suelen ser más numerosas que otros tipos de puebas.

### Herramientas:

1. __unittest:__ El módulo de pruebas unitarias integrado en la biblioteca estándar de Python. Proporciona una estructura para escribir y ejecutar pruebas unitarias.

2. __pytest:__ Un framework de pruebas popular que facilita la escritura y ejecución de pruebas unitarias. Ofrece características adicionales y una sintaxis más concisa en comparación con unittest

3. __doctest:__ Un módulo que permite escribir pruebas dentro de la documentación de funciones y métodos utilizando el formato de ejemplo interactivo de Python

## Pruebas de integración

Estas pruebas se enfocan en verificar la interacción y la integración correcta entre diferentes componentes o módulos del software.

Se prueban los flujos de trabajo y las interfaces entre las unidades de código. Las pruebas de integración pueden ser más lentas que las pruebas unitarias, ya que involucran más componentes, pero aún se espera que sean rápidas y eficientes.

### Herramientas:

1. __pytest:__ Además de pruebas unitarias, pytest también puede ser utilizado para escribir y ejecutar pruebas de integración. Proporciona características avanzadas como fixtures y marcadores que facilitan la creación y organización de pruebas de integración.

2. __Mock/MagicMock:__ Estas bibliotecas permiten crear objetos simulados(mocks) o magos(magic mocks) para reemplazar componentes del sistema durante las pruebas de integración y simular su comportamiento.


## Pruebas de interfaz de usuario

En la parte superior de la pirámide se encuentran las pruebas de interfaz de usuario. Estas pruebas se centran en verificar __la funcionalidad del software desde la perspectiva del usuario final__.

Las pruebas de interfaz de usuario pueden incluir pruebas manuales o automátizadas que simulan acciones y verifican resultados a través de la interfaz gráfica del usuario. Estas pruebas son más lentas y frágiles en comparación con las pruebas de las capas inferiores de la Piramide.

### Herramientas:

1. __Selenium:__ Una biblioteca muy utilizada para realizar pruebas de interfaz de  usuario en navegadores web. Permite simular acciones de navegación, interacción con elementos de página y verificación de resultados.

2. __Pyppeteer/Playwright:__ Herramientas que ofrecen control automátizado de navegadores web basados en Chromium(Pyppeteer) o multi-navegador(Playwright) para realizar pruebas de interfaz de usuario.


# Desarrollo guiado por Pruebas

