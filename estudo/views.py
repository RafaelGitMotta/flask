from estudo import app, db

from flask import render_template, url_for, request, redirect

from estudo.models import Contato
from estudo.forms import ContatoForm

@app.route('/') #rota é todo o caminho depois da / . Se a / estiver sozinha define a URL raiz. (@ define como decoretor)   

def homepage(): # Função que vai renderizar a página
    usuario = 'Joaquim'
    idade = 15
    return render_template('index.html', usuario=usuario,idade = idade)

#___________________________________________________

@app.route('/contato', methods=['POST','GET'])
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

   