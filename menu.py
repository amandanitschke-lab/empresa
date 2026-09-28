from departamento import *


def menu_departamento():

    while True:

        print("\n================================")
        print("         DEPARTAMENTO")
        print("================================")
        print("1 - INSERIR")
        print("2 - ATUALIZAR")
        print("3 - DELETAR")
        print("4 - LER TODOS")
        print("5 - PESQUISAR")
        print("0 - VOLTAR")

        opcao = input("Escolha: ")

        if opcao == "1":
            inserir_departamento()

        elif opcao == "2":
            atualizar_departamento()

        elif opcao == "3":
            deletar_departamento()

        elif opcao == "4":
            listar_departamentos()

        elif opcao == "5":
            pesquisar_departamento()

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_departamento()