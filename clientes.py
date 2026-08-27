#Cadastrar/listar clientes
'''Responsável pelo cadastro e gerenciamento dos clientes da locadora.
Deve permitir cadastrar um cliente informando nome e telefone.
Também deve permitir listar todos os clientes cadastrados. cadastrar_cliente e listar_clientes.''' 

import time #só pra ficar bonitinho na execução

clientes = []

def cadastrar_cliente (nome, telefone):
    cliente = {
        "nome": nome,
        "telefone": telefone
    }
    clientes.append (cliente)
    return cliente

def listar_clientes (clientes):

        if not clientes:
            print("\n[Lista vazia s]")
            time.sleep (1.5)
            return

        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            time.sleep (1.5)