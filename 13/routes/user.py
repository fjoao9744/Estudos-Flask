from flask import Blueprint

user_route = Blueprint('user', __name__)

@user_route.route('/')
def lista_usuarios():
    pass
@user_route.route('/', methods=["POST"])
def inserir_usuarios():
    pass
@user_route.route('/<str:user_id>')
def inserir_usuarios(user_id):
    pass

'''




/users/ (GET) -> lista de usuaruios
/users/ (POST) -> inserir usuario no server
/users/new (GET) -> criar um usuario
/users/<id> (GET) -> mostrar o perfil do usuario
/users/<id>/edit (GET) -> mostrar um formulario para alterar o perfil
/users/<id>/atualizar (PUT) -> atualiza os dados do cliente
/users/<id>/delete (DELETE) -> deleta um perfil



'''