from estudo import app, db

from flask import render_template, url_for, request, redirect

#render template: renderiza arquivos HTML

from datetime import datetime

from flask_login import login_user, logout_user, current_user

from estudo.models import Agendamento

# Importação dos formulários criados no arquivo forms.py (Fomulário de Contato, Usuário e Login)

from estudo.forms import UserForm,LoginForm
#____________________________________________________
#PAGINA PRINCIPAL

@app.route('/', methods=['GET','POST']) #rota é todo o caminho depois da / . Se a / estiver sozinha define a URL raiz. (@ define como decoretor)   

def homepage(): # Função que vai renderizar a página
    form = LoginForm()  #form recebe o formulário de login importado de forms.py
    if form.validate_on_submit():
        user = form.login() #recupera o usuário
        login_user(user,remember=True)
                
    return render_template('index.html', form=form)

@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user,remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form = form)
#____________________________________________________

@app.route('/agendar', methods=['GET', 'POST'])
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

@app.route('/sair/')
def logout(): 
    logout_user()
    return redirect(url_for('homepage'))

#___________________________________________________



