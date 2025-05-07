from estudo import db # Importando o db = SQLAlchemy(app) do arquivo __init__.py
from sqlalchemy import delete

from datetime import datetime

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