from flask import Flask, request
from models import Atividades, Pessoas
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# retorna todas as atividades feitas por aquele usuário
class Responsável(Resource):
    def get(self, pessoa):
        lista_user = []
        pessoas = Pessoas.query.filter_by(nome=pessoa).first()
        atividade = Atividades.query.all()
        try:
            for i in atividade:
                if i.pessoa == pessoas:
                    lista_user.append(i.nome)

            response = {
                "responsável": pessoas.nome,
                "atividade": lista_user
            }
        except:
            response =  {
                'status': 'error',
                "mensagem": 'Ocorreu um erro desconhecido na sua consulta'

            }
        return response



api.add_resource(Responsável, '/atividades/<string:pessoa>/')


if __name__ == '__main__':
    app.run(debug=True)
