from estudo import db, login_manager # Importando o db = SQLAlchemy(app) do arquivo __init__.py

from datetime import datetime

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True) 
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)


# Criando a tabela de Contatos (herda do banco de dados da classe Models). Isso informa ao flask que essa classe um Banco de Dados.
class Contato(db.Model):

    # Atributos:
    # Colunas
    id = db.Column(db.Integer,primary_key=True) #Coluna tipo (numero inteiro, chave primaria)
    data_envio = db.Column(db.DateTime, default=datetime.now()) # (Define a data de criacao do banco de dados com sendo a data do momento atual.)
    nome = db.Column(db.String, nullable=True) # tipo (letras, nao pode ser vazia)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer,default = 0)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Agendamento {self.nome} em {self.data_hora}>"
# Crie as tabelas no banco de dados (será executado na primeira vez)
#with app.app_context():
#    db.create_all()