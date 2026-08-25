#Cadastrar/listar clientes
'''Responsável pelo cadastro e gerenciamento dos clientes da locadora.
Deve permitir cadastrar um cliente informando nome e telefone.
Também deve permitir listar todos os clientes cadastrados. cadastrar_cliente e listar_clientes.''' 

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
            print("[Lista vazia]")
            return

        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")