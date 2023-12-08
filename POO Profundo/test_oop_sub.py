from test_oop_base import Reporte

class GR(Reporte):
    def __init__(self, dos:int) -> None:
        self.name = ''
        self.ano = 0
        self.day = dos

    def call_year(self):
        print(f'valor: {self.ano}')


repo = GR(2)
repo.call_year()
print(repo.day)
repo.find_day()
repo.modify_variables()
print(repo.day)