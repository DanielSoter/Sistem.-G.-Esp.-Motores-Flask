from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, PasswordField, SelectField,
                            StringField, SubmitField, TextAreaField)
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from app.models import Atividade, Clientes, Motores, Usuario


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email(),
        DataRequired("o campo 'Email' é obrigatório") 
    ])
    senha = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters."),
        DataRequired("o campo 'Senha' é obrigatório")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar", render_kw={"class": "btn btn-primary"})


class RegistroUsuarioForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cargo = StringField("Cargo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    senha = PasswordField("Senha", validators=[
        Length(6, 12, "O campo deve conter entre 6 á 12 caracters.")
    ])
    submit = SubmitField("Cadastrar")


class EdicaoUsuarioForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cargo = StringField("Cargo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    submit = SubmitField("Salvar")


class RedefUsuarioForm(FlaskForm):
    senha = PasswordField("Senha", validators=[
        Length(6, 12, "O campo deve conter entre 6 á 12 caracters."),
        EqualTo('cofirmacao_senha', message='Senhas não correspondem')
    ])
    cofirmacao_senha = PasswordField("Senha", validators=[
        Length(6, 12, "O campo deve conter entre 6 á 12 caracters.")
    ])
    submit = SubmitField("Redefinir")


class RegistroClienteForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    cpf = StringField("CPF", validators=[
        DataRequired("o campo é obrigatório")
    ])
    endereco = StringField("Endereço", validators=[
        DataRequired("o campo é obrigatório")
    ])
    telefone = StringField("Telefone", validators=[
        DataRequired("o campo é obrigatório")
    ])
    submit = SubmitField("Cadastrar")


class EditarClienteForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    cpf = StringField("CPF", validators=[
        DataRequired("o campo é obrigatório")
    ])
    endereco = StringField("Endereço", validators=[
        DataRequired("o campo é obrigatório")
    ])
    telefone = StringField("Telefone", validators=[
        DataRequired("o campo é obrigatório")
    ])
    submit = SubmitField("Salvar")


class RegistroMotorForm(FlaskForm):

    equipamento = StringField("Equipamento", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cliente = SelectField("Cliente")
    marca = StringField("Marca", validators=[
        DataRequired("o campo é obrigatório")
    ])
    modelo = StringField("Modelo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    ip = StringField("IP", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cv = StringField("CV", validators=[
        DataRequired("o campo é obrigatório")
    ])
    rpm = StringField("RPM", validators=[
        DataRequired("o campo é obrigatório")
    ])
    corrente = StringField("Corrente", validators=[
        DataRequired("o campo é obrigatório")
    ])
    submit = SubmitField("Cadastrar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cliente.choices = [ 
            (clientes.nome, clientes.nome) for clientes in Clientes.query.all()
        ]


class EditarMotorForm(FlaskForm):

    equipamento = StringField("Equipamento", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cliente = SelectField("Cliente")
    marca = StringField("Marca", validators=[
        DataRequired("o campo é obrigatório")
    ])
    modelo = StringField("Modelo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    ip = StringField("IP", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cv = StringField("CV", validators=[
        DataRequired("o campo é obrigatório")
    ])
    rpm = StringField("RPM", validators=[
        DataRequired("o campo é obrigatório")
    ])
    corrente = StringField("Corrente", validators=[
        DataRequired("o campo é obrigatório")
    ])
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cliente.choices = [ 
            (clientes.nome, clientes.nome) for clientes in Clientes.query.all()
        ]


class RegistroAtividadeForm(FlaskForm):

    ordem_servico = StringField("OS", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cliente = SelectField("Cliente")
    usuario = SelectField("Técnico")
    motor = SelectField("Motor")
    data_inicio = DateField("Data inicio", format="%Y-%m-%d")
    status = SelectField("status", choices = [('Aguardando'),('Em Andamento'), ('Concluído'), ('Pausado'), ('Cancelado')])
    data_fim = DateField("Data inicio", format="%Y-%m-%d")
    conclusao = TextAreaField("Relatório")
    submit = SubmitField("Cadastrar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cliente.choices = [
            (clientes.nome, clientes.nome) for clientes in Clientes.query.all()
        ]
        self.usuario.choices = [
            (usuarios.nome, usuarios.nome) for usuarios in Usuario.query.all()
        ]
        self.motor.choices = [
            (motores.equipamento, motores.equipamento) for motores in Motores.query.all()
        ]


class EditarAtividadeForm(FlaskForm):

    ordem_servico = StringField("OS", validators=[
        DataRequired("o campo é obrigatório")
    ])
    cliente = SelectField("Cliente")
    usuario = SelectField("Técnico")
    motor = SelectField("Motor")
    data_inicio = DateField("Data inicio", format="%Y-%m-%d")
    status = SelectField("status", choices = [('Aguardando'),('Em Andamento'), ('Concluído'), ('Pausado'), ('Cancelado')])
    data_fim = DateField("Data término", format="%Y-%m-%d")
    conclusao = TextAreaField("Relatório")
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cliente.choices = [
            (clientes.nome, clientes.nome) for clientes in Clientes.query.all()
        ]
        self.usuario.choices = [
            (usuarios.nome, usuarios.nome) for usuarios in Usuario.query.all()
        ]
        self.motor.choices = [
            (motores.equipamento, motores.equipamento) for motores in Motores.query.all()
        ]
