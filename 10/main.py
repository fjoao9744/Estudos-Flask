from flask import Flask, url_for
app = Flask(__name__) 



@app.route("/") 
def pagina_inicial(): 
    return f'<a href="{ url_for('pagina01') }">clique aqui</a>'

@app.route("/pag01")
def pagina01():
    return 'pagina 01'


if __name__ == '__main__':
    app.run(debug = True, port=9744) 

