class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}"

pessoa = Pessoa("koku", 25)
print(pessoa)

pessoa.set_nome("yuna")
pessoa.set_idade(23)

print(pessoa)
