#Menu e funcionamento geral do programa
'''Cadastrar jogo
Listar jogos
Cadastrar cliente
Listar clientes
Realizar locação
Listar locações
Sair'''


from clientes import cadastrar_cliente, listar_clientes, clientes
from jogos import cadastrar_jogo, listar_jogos, jogos
from locacoes import realizar_locacao, listar_locacoes, locacoes

from persistencia import (salvar_jogos, carregar_jogos, salvar_clientes, carregar_clientes,
                          salvar_locacoes, carregar_locacoes)

clientes.extend(carregar_clientes())
jogos.extend(carregar_jogos())
locacoes.extend(carregar_locacoes())


def menu():
    while (True):
        print("\n---MENU---")
        print("[1] - Cadastrar clientes.")
        print("[2] - Cadastrar jogos.")
        print("[3] - Listar clientes.")
        print("[4] - Listar jogos.")
        print("[5] - Listar locações.")
        print("[6] - Sair.")

        opcao = input("Tecle a opção desejada: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            cadastrar_cliente(nome, telefone)


        elif opcao == '2':
            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")
            genero = input("Gênero: ")
            valor = float(input("Valor do jogo: "))
            locacao_dia = float(input("Valor da locação por dia: "))

            cadastrar_jogo(titulo, plataforma, genero, valor, locacao_dia)

        elif opcao == '3':
            listar_clientes(clientes)

        elif opcao == '4':
            listar_jogos(jogos)

        elif opcao == '5':
            listar_locacoes()

        elif opcao == '6':
            break

        else:
            print("\n[Opção Inválida]")

menu ()