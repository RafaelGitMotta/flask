from estudo import app, db

from flask import render_template, url_for, request

from estudo.models import Contato

@app.route('/') #rota é todo o caminho depois da / . Se a / estiver sozinha define a URL raiz. (@ define como decoretor)   

def homepage(): # Função que vai renderizar a página
    usuario = 'Joaquim'
    idade = 15
    return render_template('index.html', usuario=usuario,idade = idade)

@app.route('/contato', methods=['GET','POST'])
def novapagina():
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

        db.session.add(contato)
        db.session.commit()

        
    return render_template('contato.html', contex=contex)
    
   