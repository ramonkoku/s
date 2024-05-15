class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def alterar_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("A nova senha atende aos critérios de segurança.")

# Exemplo de uso
usuario = Usuario("koku", "senha123")
print("Nome do usuário:", usuario.nome)

usuario.alterar_senha("nome")
usuario.alterar_senha("novaSenhaSegura123")
