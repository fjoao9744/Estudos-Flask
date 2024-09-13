from flask import Blueprint

user_route = Blueprint('user', __name__)

@user_route.route('/')
def lista_usuarios():
    return "lista de usuarios"
@user_route.route('/', methods=["POST"]) #inserir os dados do cliente no banco de dados
def inserir_usuarios():
    pass
@user_route.route('/new') #formulario para criar um user
def form_cliente():
    return {"pagina":"formulario de usuarios"}

@user_route.route('/<int:user_id>') #pegando o id de um usuario
def user(user_id):
    #exibir detalhes do cleinte
    pass

@user_route.route('/<int:user_id>/edit') #formulario para editar um perfil de usuario
def edit_user(user_id):
    pass

@user_route.route('/<int:user_id>/update', methods=["PUT"]) #atualizar o perfil do usuario
def up_user(user_id):

    pass

@user_route.route('/<int:user_id>/delete', methods=["DELETE"]) #deletando um usuario
def del_user(user_id):

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