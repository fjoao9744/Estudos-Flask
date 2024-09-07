
from flask import Flask, render_template 
app = Flask(__name__) 


@app.route("/") 
def pagina_inicial(): 
    return render_template("pagina-inicial.html") 


@app.route("/alunos")
def alunos():
    return render_template("alunos.html") 


@app.route("/alunos/<nome_aluno>") #se colocar <> vai ficar dinamico, ou seja, vai mudar
def usuarios(nome_aluno): #recebe o parametro que vai ser a variavel que vai mudar
    return f'<h1>bem vindo {nome_aluno}<h1>'


if __name__ == '__main__':
    app.run(debug = True) 