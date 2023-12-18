class Nodo(object):
    def __init__(self, dato=None, prox = None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)
    
def verLista(nodo):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras nodo no es None
    while nodo:
        # muestra el dato
        print(nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox
    print('\n')
        
if __name__ == '__main__':
    v3 = Nodo("Bananas")
    v2 = Nodo("Peras", v3)
    v1 = Nodo("Manzanas", v2)

    print('v3')
    verLista(v3)

    print('v2')
    verLista(v2)

    print('v1')
    verLista(v1)

    print('lista')
    lista=v1
    verLista(lista)

    print('lista.prox')
    lista=lista.prox
    verLista(lista)

    