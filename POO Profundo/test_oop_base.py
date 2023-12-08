class Reporte:

    def __init__(self) -> None:
        self.data = None
        self.day = 0

    def find_day(self):
        print(f'método en la clase valor: {self.day}')

    def modify_variables(self):
        self.day += 1
        print(f"Aumentar {self.day}")
