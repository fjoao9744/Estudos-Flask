from flask import Flask

app = Flask(__name__) #obrigatorio

'''
toda pagina tem um caminho(route) que é oque vem depois do dominio
função é oque vai ser exibido na pagina

'''

@app.route("/") #decorator para indicar que é do site essa função
def pagina_inicial(): #criação da pagina inicial
    return "esse é o meu primeiro site em flask"

if __name__ == '__main__': #para evitar problemas
    app.run(debug = True) #colocar no ar #debug -> é pra atualizar sempre

    