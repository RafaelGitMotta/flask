# O Arquivo Models é responsável  por fazer a comunicação da aplicação flask com o banco de dados.
#Criando os bancos de dados em Python que posteriormente serão convertidos em linguagem SQL pelo próprio Python. 

from estudo import db, login_manager # Importando a variável db = SQLAlchemy(app) e a variável login_manager do arquivo __init__.py

from datetime import datetime

from flask_login import UserMixin #UserMixin é o modelo que será usado para 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

#----------------------------------------------------

#Essa função recupera o usuário para fazer a sessão de login
@login_manager.user_loader
def load_user(user_id):# recebe um id
    return User.query.get(user_id)# retorna o usuário logado
#____________________________________________________
# Banco de Dados dos Usuários

class User(db.Model, UserMixin):# o Usermixin informa para o aplicatico que essa tabela é para controle de login, no caso será usado o campo de email para controle de login, mas poderia ser escolhido qualquer um dos cfampos abaixo
    id = db.Column(db.Integer,primary_key=True) 
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String(150), nullable=True)
    password_hash = db.Column(db.String, nullable=True)

    def set_password(self, password):
        self.password_hash  = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# Após escrever no arquivo models.py o banco de dados acima é preciso criar esse modelo no banco de dados, primeiro é preciso montar o banco de dados usando o seguinte comando no terminal:flask db migrate
#Depois é preciso fazer o upload desse banco de dados montado usando o seguinte comando no terminal:flask db upgrade 

#Depois é preciso criar o formulário no forms.py
#__________________________________________________


# Criando a tabela de Contatos (herda do banco de dados da classe Models). Isso informa ao flask que essa classe um Banco de Dados.
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Agendamento {self.nome} em {self.data_hora}>"
# Crie as tabelas no banco de dados (será executado na primeira vez)
#with app.app_context():
#    db.create_all()