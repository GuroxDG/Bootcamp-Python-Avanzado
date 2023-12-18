class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """
        self.items.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su
            valor. Si la cola está vacía, levanta ValueError. """
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
        
    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.items == []
    
    def cantidad(self):
        return len(self.items)
    
if __name__ == '__main__':
    pila = Cola()
    print(pila.es_vacia())
    pila.encolar(2)
    pila.encolar(3)
    pila.encolar(4)
    print(pila.items)
    print(pila.cantidad())
    print(pila.desencolar())
    print(pila.items)
    print(pila.cantidad())