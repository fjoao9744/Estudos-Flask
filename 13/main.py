from flask import Flask, url_for, render_template
app = Flask(__name__) 



@app.route("/") 
def pagina_inicial(): 
    titulo = "teste 01"
    usuarios = [
        {'nome':'smogon', 'ativo': True},
        {'nome':'joao', 'ativo': True},
        {'nome':'maria', 'ativo': False},
        {'nome':'capa', 'ativo': False}
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route("/pag01")
def pagina01():
    return 'pagina 01'


if __name__ == '__main__':
    app.run(debug = True, port=9744) 

