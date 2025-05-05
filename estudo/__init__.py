from flask import Flask #da biblioteca flask importe a classe Flask

from flask_sqlalchemy import SQLAlchemy
# Dá biblioteca Flask SQL Alchemy importe a classe SQLAlchemy
from flask_migrate import Migrate
# Dá biblioteca flask migrate importe a classe Migrate

app = Flask(__name__)
 # Start no aplicativo, (_name_) Pega o nome do aplicativo a partir do nome do arquivo no qual se está trabalhando no caso o arquivo "main".

#Definindo a onde vai ficar o banco de dados:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# Pegando a URI colocando na configuração de aplicativo e definindo qual que é o caminho e criando o arquivo database.db junto do main
app.config['SQKALCHEMY_TRACK_MODIFICATIONS'] = False

# Definindo a várial de banco de dados
db = SQLAlchemy(app)
#para nossso aplicativo eu quero criar o banco de dados descrito nas configurações acima

#Definindo a aplicativo de migrate para atualização.
migrate = Migrate(app,db)


from estudo.views import homepage
from estudo.models import Contato