from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import  HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

USUARIO = {
    'Rafael': '123',
    'Galleani': '321'
}
# validação de usuário
#@auth.verify_password
#def verificacao(login, senha):
#    if not (login, senha):
#        return False
#    return USUARIO.get(login) == senha
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    #consultando um dado no banco de dados
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response


    # alterando o dado no banco de dados
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

        return response


    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()

        return {'status': 'sucesso', 'mensagem': f'Pessoa {nome} exluida com sucesso'}

class list_all(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome': i.nome, 'idade': i.idade}for i in pessoas]
        print(response)
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class List_atividades(Resource):

# cadastra uma nova atividade
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response

# retornas todas as atividades e seus usuarios

    def get(self):
        response = []
        atividades = Atividades.query.all()
        print(atividades)
        for i in atividades:
            if i.pessoa != None:
                response.append({
                    "id": i.id,
                    "nome": i.nome,
                    "pessoa": i.pessoa.nome
                        })
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(list_all, '/pessoa/')
api.add_resource(List_atividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)














