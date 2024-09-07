from flask import Flask, render_template 
app = Flask(__name__) 


@app.route("/") 
def pagina_inicial(): 
    return render_template("pagina-inicial.html") 

@app.route("/smogon/") 
def smogon(): 
    return "ola smogon"

@app.route("/alunos/")
def alunos():
    return render_template("alunos.html") 

@app.route("/alunos/<nome_aluno>") 
def usuarios(nome_aluno): 
    return f"ola {nome_aluno}"

if __name__ == '__main__':
    app.run(debug = True) 