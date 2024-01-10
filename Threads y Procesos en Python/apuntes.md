# Temas

* ¿Qué son los Threads y procesos?
* Creación de Threads
* Comunicación de Threads
* GIL
* Procesos
* ¿Threads o procesos?
* Pool de procesos

# ¿Qué es un proceso?

* Un proceso es una instancia en ejecución de un programa
* Tiene su propio espacio de memoria, conjunto de recursos y estado
* Los procesos se crean y se administran por el sistema operativo

# ¿Qué son lso threads?

* Un Thread es una secuencia de instrucciones que se ejecutan dentro de un proceso
* Un proceso puede tener múltiples hilos que comparten el mismo espacio de memoria y recursos, lo que permite una Comunicación y sincronización más fácil entre ello
* Los hilso se ejecutan de forma concurrente

## ¿Concurrencia? ¿Paralelismo?
* __Concurrencia:__ Cuando 2 o más tareas están ocurriendo al mismo tiempo.
* __Paralelismo:__ Cuando 2 o más tareas están ocurriendo juntas al mismo tiempo
* Todo proceso debe tener al menos un thread

# Proceblemas con Threads

* Race Condition (falso negativos o falsos positivos dado que modifican la información al mismo tiempo)
* Computacionalmente hablanod es caro crear un thread
* El race condition se puede mitigar con estrategias como Lock

# Clase Event

La clase event proporciona un mecanismo para que lso hilso esperen hasta que se active un evento específico.

```
from  threading import Event
event = Event()

event.set()
event.wait()
```