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
        print("[3] - Realizar locações.")
        print("[4] - Listar clientes.")
        print("[5] - Listar jogos.")
        print("[6] - Listar locações.")
        print("[7] - Sair.")

        opcao = input("Tecle a opção desejada: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            cadastrar_cliente(nome, telefone)

            cadastrar_cliente(nome, telefone)
            salvar_clientes(clientes)

            print("\n[Cliente cadastrado com sucesso!]")

        elif opcao == '2':
            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")
            genero = input("Gênero: ")
            valor = float(input("Valor do jogo: "))
            locacao_dia = float(input("Valor da locação por dia: "))

            cadastrar_jogo(titulo, plataforma, genero, valor, locacao_dia)
            salvar_jogos(jogos)

            print("\n[Jogo cadastrado com sucesso!]")

        elif opcao == '3':
            titulo = input("Digite o título do jogo: ")
            nome = input("Digite o nome do cliente: ")

            jogo_encontrado = None
            cliente_encontrado = None

            for jogo in jogos:
                if jogo['titulo'].lower() == titulo.lower():
                    jogo_encontrado = jogo
                    break

            for cliente in clientes:
                if cliente['nome'].lower() == nome.lower():
                    cliente_encontrado = cliente
                    break

            if jogo_encontrado is None:
                print("\n[Jogo não encontrado]")

            elif cliente_encontrado is None:
                print("\n[Cliente não encontrado]")

            else:
                dias = int(input("Por quantos dias você deseja alugar o jogo? "))

                realizar_locacao(jogo_encontrado, dias, cliente_encontrado)
                salvar_locacoes(locacoes)

                print("\n[Locação realizada com sucesso!]")

        elif opcao == '4':
            listar_clientes(clientes)

        elif opcao == '5':
            listar_jogos(jogos)

        elif opcao == '6':
            listar_locacoes()

        elif opcao == '7':
            break

        else:
            print("\n[Opção Inválida]")

menu ()