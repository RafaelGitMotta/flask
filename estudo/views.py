from estudo import app, db

from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user

from estudo.models import Contato

# Importação dos formulários criados no arquivo forms.py (Fomulário de Contato, Usuário e Login)

from estudo.forms import ContatoForm, UserForm,LoginForm
#____________________________________________________
#PAGINA PRINCIPAL

@app.route('/', methods=['GET','POST']) #rota é todo o caminho depois da / . Se a / estiver sozinha define a URL raiz. (@ define como decoretor)   

def homepage(): # Função que vai renderizar a página
    form = LoginForm()  #form recebe o formulário de login importado de forms.py
    if form.validate_on_submit():
        user = form.login() #recupera o usuário
        login_user(user,remember=True)

    return render_template('index.html', form=form)
#____________________________________________________

#CADASTRO

@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user,remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form = form)
#___________________________________________________
# View para p Logout

@app.route('/sair/')
def logout(): 
    logout_user()
    return redirect(url_for('homepage'))

#___________________________________________________

@app.route('/contato', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    contex = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        
    

         
    return render_template('contato.html', contex=contex, form=form)




#___________________________________________________
@app.route('/contato/lista/')
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by('nome')
    if pesquisa !='':
        dados = dados.filter_by(nome=pesquisa)
    
    context = {'dados': dados.all()}

    return render_template('contato_lista.html', context=context)
#___________________________________________________

@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj = Contato.query.get(id) 
    
    return render_template('contato_detail.html', obj=obj)
 

#_______________________________________________________________________   
# Formato nao recomendado 


@app.route('/contato_old', methods=['GET','POST'])
def contato_old():
    
    contex = {}

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET :',pesquisa)
        contex.update({'pesquisa' : pesquisa})
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem) 

        db.session.add(contato_old)
        db.session.commit()

         
    return render_template('contato_old.html', contex=contex)

   