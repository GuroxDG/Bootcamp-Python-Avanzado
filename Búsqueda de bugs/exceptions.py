
def division(number_one, number_two):
    try:
        return print((number_one / number_two))
    except TypeError as err:
        print("Error de tipo")
    except ZeroDivisionError as err:
        print("No es posible dividir por cero")

if __name__ == '__main__':
    division(20, 30)
    division('20', 30)
    division(20, 0)