from collections import deque

class Cola:

    def __init__(self) -> None:
        self.lista = deque()

    def lista_vacia(self):
        return len(self.lista) == 0
    
    def agregar_elemento(self, elemento):
        self.lista.append(elemento)

    def quitar_elemento(self):
        if self.lista_vacia():
            return None
        return self.lista.popleft()

    def cantidad(self):
        return len(self.lista) 
    
if __name__ == '__main__':
    pila = Cola()
    print(pila.lista_vacia())
    pila.agregar_elemento(2)
    pila.agregar_elemento(3)
    pila.agregar_elemento(4)
    print(pila.lista)
    print(pila.cantidad())
    print(pila.quitar_elemento())
    print(pila.lista)
    print(pila.cantidad())