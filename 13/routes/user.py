from flask import Blueprint

user_route = Blueprint('user', __name__)

@user_route.route('/')
def lista_usuarios():

@user_route.route('/<str:user_id>')
def obter_usuarios(user_id):

    