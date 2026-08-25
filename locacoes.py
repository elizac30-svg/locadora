#Fazer locação, calcular desconto e listar locações
'''Responsável pelo gerenciamento das locações realizadas.
Deve permitir realizar uma locação informando o cliente, o jogo e a quantidade de dias.
Deve calcular automaticamente o valor total da locação, aplicar o desconto correspondente ao período e
registrar a locação.
Também deve permitir listar todas as locações realizadas.
Regras de desconto:
Até 3 dias → 0%
Acima de 3 dias → 5%
Acima de 7 dias → 10%.

calcular_desconto(dias) → determina a porcentagem de desconto.
calcular_valor_locacao(jogo, dias) → calcula o valor da locação e aplica o desconto.
listar_locacoes() → mostra o histórico de locações.'''

import time #só pra ficar bonitinho na execução

from jogos import jogos
from clientes import clientes

locacoes = []

def calcular_desconto (dias):

    if dias > 7:
            return 0.10
    elif dias > 3:
        return 0.05
    else:
        return 0

def realizar_locacao (jogo, dias, cliente):

    dias = int(input("Por quantos dias você deseja alugar o jogo? "))

    valor_inicial = jogo['locacao_dia'] * dias

    porcentual_desconto = calcular_desconto (dias)
    valor_desconto = valor_inicial * porcentual_desconto

    total_venda = valor_inicial - valor_desconto

#lembrete por: Jogo, Plataforma, Cliente, Quantidade de dias, Valor inicial, Desconto, Valor final

    venda = {
        "jogo": jogo['titulo'],
        "plataforma": jogo['plataforma'],
        "cliente": cliente['nome'],
        "quantidade_dias": dias,
        "valor_inicial": valor_inicial,
        "desconto": porcentual_desconto,
        "valor_final": total_venda
    }

    locacoes.append (venda)
    time.append (1.5)
    return venda 

def listar_locacoes ():

    if not locacoes:
        print("\n[Lista vazia]")
        time.sleep (1.5)
        return


    for venda in locacoes:
        print("\n---NOTINHA---")
        print(f"Jogo: {venda['jogo']}")
        print(f"Plataforma {venda['plataforma']}")
        print(f"Cliente: {venda['cliente']}")
        print(f"Quantidade de dias: {venda['quantidade_dias']}")
        print(f"Valor inicial: {venda['valor_inicial']:.2f}")
        print(f"Desconto: {venda['desconto']:.2f}")
        print(f"VALOR TOTAL: {venda['valor_final']:.2f}")
