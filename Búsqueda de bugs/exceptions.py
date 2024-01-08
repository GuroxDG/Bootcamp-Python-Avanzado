
def division(number_one, number_two):
    try:
        return print((number_one / number_two))
    except TypeError as err:
        print("Error de tipo", type(err))
    except ZeroDivisionError as err:
        print("No es posible dividir por cero", type(err))

class LiveErrorException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

if __name__ == '__main__':
    division(20, 30)
    division('20', 30)
    division(20, 0)

    try:
        raise LiveErrorException('Lo sentimos')
    except LiveErrorException as error:
        print(error)