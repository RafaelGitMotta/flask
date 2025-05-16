from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField #Campo tipo (texto, botao, campo de senha)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

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
    confirmacao_senha = PasswordField('Confirme a Senha',validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    #Função de validação de email: def validate_"aqui o campo que se deseja validar"
    def validade_email(self, email):
        if User.query.filter(email=email.data).first():# filtra o email dos usuário e se tiver um igual pula para o comando abaixo return mostrando a mensagem de erro.
            return ValidationError('Usuário já cadastro com esse E-mail!!!')

    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        db.session.add(user)
        db.session.commit()
        return user
   

#Criando o campo de Formulário de Login   
 
class LoginForm(FlaskForm):
    
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    password = PasswordField('Senha',validators=[DataRequired(), Length(min=6)])
    btnSubmit = SubmitField('Entrar')

# função para verificar email e senha de login


