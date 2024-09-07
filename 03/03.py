from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def pagina_inicial(): 
    return "esse é o meu site em flask"

@app.route("/alunos")
def alunos():
    alunos = ['smogon', 'joao', 'moises']
    return f"<h1>lista de alunos:</h1> \n <p> moises </p>\n <p>joão </p>\n <p>hendrick</p>"

if __name__ == '__main__':
    app.run(debug = True) 