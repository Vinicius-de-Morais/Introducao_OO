
class Heroi:

    def __init__(self, nome, poder, tamanho, estado):
        self.__nome = nome
        self.__poder = poder
        self.__tamanho = tamanho
        self.__estado = estado

    def exibe_nome(self):
        print(f'O heroi {self.__nome} está atualmente: {self.__estado}.')

    @property
    def nome(self):
        return self.__nome

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado

