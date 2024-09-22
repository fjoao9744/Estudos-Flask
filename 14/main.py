from flask import Flask, url_for, render_template
from routes.home import home_route 
from routes.user import user_route

app = Flask(__name__) 


app.register_blueprint(home_route)
app.register_blueprint(user_route, url_prefix="/user")



if __name__ == '__main__':
    app.run(debug = True, port=9744) 

