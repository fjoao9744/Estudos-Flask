#a pasta template tem que obrigatoriamente ter esse nome e armazena documentos html

from flask import Flask, render_template #colocar o render_tamplate para conseguir carregar os templates

app = Flask(__name__) 

@app.route("/") 
def pagina_inicial(): 
    return render_template("pagina-inicial.html") #carrega a pagina html

@app.route("/alunos")
def alunos():
    return render_template("alunos.html") #carrega a pagina html

if __name__ == '__main__':
    app.run(debug = True) 