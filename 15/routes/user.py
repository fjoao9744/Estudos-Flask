from flask import Blueprint, render_template, request
from database.users import USUARIOS


user_route = Blueprint('user', __name__)

@user_route.route('/') #lista de usuarios
def lista_usuarios():
    return render_template("lista-users.html", usuarios=USUARIOS)

@user_route.route('/', methods=["POST"]) #inserir os dados do cliente no banco de dados
def inserir_usuarios():
    
    data = request.json # isso ta vindo do front-end("enviar")

    new_user = {
        "id" : len(USUARIOS) + 1,
        "nome" : data["nome"],
        "email" : data["email"]
    }

    USUARIOS.append(new_user)
    return render_template("item_user.html", user=new_user)

@user_route.route('/new') #formulario para criar um user
def form_cliente():
    return render_template("new-user.html")

@user_route.route('/<int:user_id>') #pegando o id de um usuario
def user(user_id):
    #exibir detalhes do cleinte
    return render_template("user.html")

@user_route.route('/<int:user_id>/edit') #formulario para editar um perfil de usuario
def edit_user(user_id):
    return render_template("edit-user.html")
    
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