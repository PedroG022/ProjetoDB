from models.User import User
from os import system
from Utils import Menu as u, Manager

manager = Manager("./databases/data.db")


def userMenu():
    options = ["1 - Cadastrar usuário", "2 - Listar usuários",
               "3 - Deletar usuário", "4 - Voltar"]

    esc = u.menu("Gerenciamento de Usuários", options)

    match esc:
        case 1:

            user = User(
                u.inp("Nome Completo"),
                u.inp("Endereço de Email"),
                u.inp("Senha (Mínimo 6 caracteres)", password=True),
                u.inp("Data de nascimento (DD/MM/AAAA)"),
                u.inp("Subscrição (1 - MENSAL, 2 - ANUAL)"),
                u.inp("Endereço (Rua, Número, Bairro, Cidade, Estado)"),
                u.inp("Telefone (DDD + Número)"),
                u.inp("Forma de pagamento (Cartão de Crédito, Débito, Boleto)")
            )

            manager.saveUser(user)
            input("Dados salvos com sucesso! \nPressione ENTER para continuar...")

        case 2:
            manager.getUsers()
            input("Pressione ENTER para continuar...")

        case 3:
            if manager.deleteUser(u.inp("Id de usuário")):
                print("Usuário deletado com sucesso!")
            else:
                print("Usuário não encontrado!")
            input("Pressione ENTER para continuar...")

    return


def mainMenu():
    return u.menu("Menu Principal", ["1 - Gerenciar usuários", "2 - Sair"])


if __name__ == "__main__":

    while True:
        match mainMenu():
            case 1:
                userMenu()
            case 2:
                manager.close()
                system("clear")
                exit()
            case _:
                print("Opção inválida")
