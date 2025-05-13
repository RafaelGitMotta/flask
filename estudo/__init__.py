# ARQUIVO DE INICIALIÇÃO DA APLICAÇÃO.

from flask import Flask #A partir da biblioteca flask importe a classe Flask

from flask_sqlalchemy import SQLAlchemy
# A partir biblioteca Flask SQL Alchemy importe a classe SQLAlchemy
from flask_migrate import Migrate
# A partir biblioteca flask migrate importe a classe Migrate

from dotenv import load_dotenv

from flask_login import LoginManager
from flask_bcrypt import Bcrypt


import os
load_dotenv('.env')


app = Flask(__name__) # Flask(Main)
 # Inicia no aplicativo, (_name_) Pega o nome do aplicativo a partir do nome do arquivo no qual se está trabalhando no caso o arquivo "main".

#O comanado abaixo definea onde vai ficar o banco de dados:(Sem Variáveis de Ambiente)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#Com Váriáveis de Ambiente
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


# Pegando a URI colocando na configuração de aplicativo e definindo qual que é o caminho e criando o arquivo database.db junto do main
app.config['SQKALCHEMY_TRACK_MODIFICATIONS'] = False 
# Desativa a checagem automatica de modifiacoes


#________________________________________________
#(Sem Variáveis de Ambiente)
#app.config['SECRET_KEY'] = '12345werefewfwefw-fsffefffe67890'

#(Com Váriaveis de Ambiente)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#===================================================#

# Definindo a váriavel de banco de dados

db = SQLAlchemy(app)
# Para nossso aplicativo eu quero criar o banco de dados descrito nas configurações acima. Essa variável será usada pelo arquivo Models.py

#Definindo a aplicativo de migrate para atualização.
migrate = Migrate(app,db)

#Configuração do Login
login_manager = LoginManager(app) #a variável login_manager recebe o LoginManager (adiciona o aplicativo). Essa variável será usada pelo arquivo Models.py

# Controle de acesso a diferentes partes da aplicação.
login_manager.login_view = 'homepage'

#Configuração do Bcrypt, responsável por encriptar a senha do usuário
bcrypt = Bcrypt(app)

from estudo.views import homepage
