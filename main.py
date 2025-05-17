from estudo import app # Importa a variável app da pasta estudo no arquivo __init__.py que recebe o Flask

if __name__ == '__main__':# SE __name__ for igual a __main__(entao o pragrama executa a alinha de baixo)
    app.run(debug=True)# app.run executa a variavel app e faz a aplicação rodar.(debub=True) faz com que a cada atualização restarta a aplicação.

#DEBUB_MODE = os.getenv('DEBUG_MODE')=='True'