from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField #Campo tipo (texto, botao, campo de senha)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

#EqualTo srve para verificar se a senha digitada no campo senha é igual ao do campo digitar senha.

#ValidationError serve para verifica se não tem 2 emails iguais ao cadastrar

from estudo import db, bcrypt
from estudo.models import User

#____________________________________________________

#Cria o formulário de Usuário

class UserForm(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired()])
    sobrenome = StringField('Sobrenome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    confirmacao_senha = PasswordField('Senha',validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    #Função de validação de email: def validate_"aqui o campo que se deseja validar"
    def validade_email(self, email):
        if User.query.filter(email=email.data).first():# filtra o email dos usuário e se tiver um igual pula para o comando abaixo return mostrando a mensagem de erro.
            return ValidationError('Usuário já cadastro com esse E-mail!!!')
#___________________________________________________ 
# Função para salvar a senha criptografada no banco de dados       
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))#bcrypt.generate_password_hash criptografa a senha(self.senha.data.encode('utf-8') é a senha passada pelo usuário encodada no padrao de escrita utf-8 para receber caracteres especiais)

        #cria um usuário recebendo os dados do formulário com a senha já criptografada
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha # senha recebe a senha já criptografada
        )
        # Agora a senha criptografada será salva no banco de dados
        db.session.add(user)
        db.session.commit()
        return user # retorna o usuário que acabou de ser salvo no banco de dados.
#___________________________________________________

#Criando o campo de Formulário de Login   
 
class LoginForm(FlaskForm):
    
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

# função para verificar email e senha de login
    def login(self): 
        #Recuperar o usuário do e-mail
        user =User.query.filter_by(email=self.email.data).first()
        # pegando o usuário de acordo com o e-mail digitado

        #Verificar se a senha é válida
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                #Retorna o Usuário 
                return user #Retorna o Usuário
            else:
                raise Exception('Senha Incorreta!!!')               
        else:
            raise Exception('Usuário não encontrado!!!')
#____________________________________________________

### class ContatoForm(FlaskForm):
#    nome = StringField('Nome',validators=[DataRequired()])
#    email = StringField('E-mail',validators=[DataRequired(), Email()])
#    assunto = StringField('Assunto',validators=[DataRequired()])
#    mensagem = StringField('Mensagem',validators=[DataRequired()])
#    btnSubmit = SubmitField('Enviar',validators=[DataRequired()])

 #   def save(self):
 #       contato = Contato(
 #       nome = self.nome.data,
 #       email = self.email.data,
  #      assunto = self.assunto.data,
  #      mensagem = self.mensagem.data
  #      )

  #      db.session.add(contato)
  #      db.session.commit()


