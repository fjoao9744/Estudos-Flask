from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def pagina_inicial(): 
    return "esse é o meu primeiro site em flask"

@app.route("/alunos") #criando uma nova pagina
def alunos():
    alunos = ['smogon', 'joao', 'moises']
    return f"lista de alunos: {alunos}"

if __name__ == '__main__':
    app.run(debug = True) 