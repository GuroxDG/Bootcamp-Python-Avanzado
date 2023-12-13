def busqueda_lineal(lista, valor_buscado):
    for i in range(len(lista)):
        print(i, lista[i], val)
        if lista[i] == valor_buscado:
            return True
            break
        print('No coincide')
    
if __name__ == '__main__':
    lista = [i for i in range(0,11)]
    val = 7

    print(busqueda_lineal(lista, val))
