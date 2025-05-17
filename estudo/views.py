from estudo import app, db

from flask import render_template, url_for, request, flash, redirect

#render template: renderiza arquivos HTML

from datetime import datetime

from flask_login import login_user, logout_user, login_required

from estudo.models import Agendamento, User

# Importação dos formulários criados no arquivo forms.py (Fomulário de Contato, Usuário e Login)

from estudo.forms import UserForm,LoginForm

#____________________________________________________
#PAGINA PRINCIPAL

@app.route('/', methods=['GET','POST']) #rota é todo o caminho depois da / . Se a / estiver sozinha define a URL raiz. (@ define como decoretor)   
def homepage(): # Função que vai renderizar a página
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Email ou senha inválidos', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login'))

#____________________________________________________

@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user,remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form =form)
#____________________________________________________

@app.route('/agendar', methods=['GET', 'POST'])
@login_required
def agendar():
    if request.method == 'POST':
        nome = request.form['nome']
        data_str = request.form['data']
        hora_str = request.form['hora']

        try:
            data_hora_str = f"{data_str} {hora_str}"
            data_hora = datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M')

            novo_agendamento = Agendamento(nome=nome, data_hora=data_hora)
            db.session.add(novo_agendamento)
            db.session.commit()  # Salva as alterações no banco de dados
            return redirect(url_for('listar_agendamentos'))
        except ValueError:
            erro = "Formato de data ou hora inválido."
            return render_template('agendar.html', erro=erro)

    return render_template('agendar.html')
#_______________________________________________________________________

@app.route('/agendamentos')
def listar_agendamentos():
    agendamentos = Agendamento.query.order_by(Agendamento.data_hora).all()
    return render_template('listar_agendamentos.html', agendamentos=agendamentos)

if __name__ == '__main__':
    app.run(debug=True)

#___________________________________________________
# View para p Logout



