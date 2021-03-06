import re
from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy.dialects.sqlite import DATE

@login_manager.user_loader
def current_user(user_id):
    return Usuario.query.get(user_id)


#inicialmente todos os usuários serão técnicos
class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    senha = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.String(84), nullable=False)  

    def __str__(self):
        return self.nome

#Nessa tabela, assim como mensionado abaixo, eu gostaria de criar uma lista com todos os motores cadastrados.
class Clientes(db.Model, UserMixin):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    cpf = db.Column(db.String(100), nullable=True, unique=True)
    endereco = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.nome

#Aqui eu gostaria de exibir todos os motores cadastrados para os clientes.
class Motores(db.Model, UserMixin):
    __tablename__ = "motores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipamento = db.Column(db.String(84), nullable=False, index = True)
    cliente = db.Column(db.String(84), nullable=False)
    marca = db.Column(db.String(84), nullable=False)
    modelo = db.Column(db.String(84), nullable=False)
    ip = db.Column(db.String(10), nullable=False)
    cv = db.Column(db.String(10), nullable=False)
    rpm = db.Column(db.String(15), nullable=False)
    corrente = db.Column(db.String(15), nullable=False)

    def __str__(self):
        return self.equipamento

#Aqui quando eu criar a tela eu gostaria de exibir uma lista com motores(coluna equipamento), clientes(coluna nome)
#  e usuários cadastrados(coluna nome). "Está correto"
class Atividade(db.Model, UserMixin):
    __tablename__ = "atividades"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ordem_servico = db.Column(db.String(84), nullable=False, unique=True, index=True)
    cliente = db.Column(db.String(84), nullable=False)
    motor = db.Column(db.String(84), nullable=False)
    usuario = db.Column(db.String(84), nullable=False)
    data_inicio = db.Column(db.Date(), nullable=False)
    status = db.Column(db.String(84), nullable=False)
    data_fim = db.Column(db.Date(), nullable=False)
    conclusao = db.Column(db.String(200), nullable=False)

    def __str__(self):
        return self.ordem_servico

#Tabelas: usuários e atividades
#Um usuário(pai) pode ter muitas atividades(filha)

#Tabelas: clientes e motores
#Um cliente(pai) pode ter vários motores(filho)

#Tabelas: atividades, usuários, clientes e motores
#Uma atividade(pai) possui apenas um motor(filho), um usuário(filho) e um cliente(filho).

