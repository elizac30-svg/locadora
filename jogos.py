#Cadastrar/listar jogos e controlar cópias
'''Responsável pelo cadastro e gerenciamento dos jogos da locadora.
Deve permitir cadastrar um jogo informando título, plataforma, gênero e valor da locação por dia.
Também deve permitir listar todos os jogos cadastrados. cadastrar_jogo e listar_jogo.'''

jogos = []

def cadastrar_jogo(titulo, plataforma, genero, valor, locacao_dia):

    jogo = {
        "titulo": titulo,
        "plataforma": plataforma,
        "genero": genero,
        "valor": valor,
        "locacao_dia": locacao_dia
    }

    jogos.append (jogo)
    return jogo


def listar_jogos(jogos):
    for jogo in jogos:

        print(f"Título: {jogo['titulo']}")
        print(f"Plataforma: {jogo['plataforma']}")
        print(f"Gênero: {jogo['genero']}")
        print(f"Valor: {jogo['valor']}")
        print(f"Locação por dia: {jogo['locacao_dia']}")