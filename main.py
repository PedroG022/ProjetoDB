from models.User import User
from os import system
from Utils import Menu as u, Manager

manager = Manager("./databases/data.db")


def userMenu():
    options = ["1 - Cadastrar usuário", "2 - Listar usuários", "3 - Voltar"]
    esc = u.menu("Gerenciamento de Usuários\noi\n sai", options)

    match esc:
        case 1:
            user = User(
                u.ginp("Nome Completo"),
                u.ginp("Endereço de Email"),
                u.ginp("Senha (Mínimo 6 caracteres)", password=True),
                u.ginp("Data de nascimento (DD/MM/AAAA)"),
                u.ginp("Subscrição (1 - MENSAL, 2 - ANUAL)"),
                u.ginp("Endereço (Rua, Número, Bairro, Cidade, Estado)"),
                u.ginp("Telefone (DDD + Número)"),
                u.ginp("Forma de pagamento (Cartão de Crédito, Débito, Boleto)")
            )

            manager.saveUser(user)
            input("Dados salvos com sucesso! \nPressione ENTER para continuar...")

        case 2:
            manager.getUsers()
            input("vsf")
            return 0

    return


def mainMenu():
    return u.menu("Menu Principal", ["1 - Gerenciar usuários", "2 - Sair"])


if __name__ == "__main__":

    while True:
        match mainMenu():
            case 1:
                userMenu()
            case 2:
                system("clear")
                exit()
            case _:
                print("Opção inválida")
