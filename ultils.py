from models import Pessoas, db_session, Usuarios

def insere():
    pessoa = Pessoas(nome='Fabricio', idade='22')
    pessoa = Pessoas(nome='Carlos', idade='31')
    pessoa.save()

# consulta dados do user na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Fabricio').first()
    print(pessoas)
# altera algum dado do usser na tabela pessoa
def altera():
    pessoa = Pessoas.query.filter_by(nome='Fabricio').first()
    pessoa.idade = 21
    pessoa.save()
# exlcui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    pass
    #exclui_pessoa()
    # altera()
