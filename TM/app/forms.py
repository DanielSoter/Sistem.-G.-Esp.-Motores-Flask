from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, PasswordField, SelectField,
                            StringField, SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length

from app.models import Atividade, Clientes, Motores, Usuario


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
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


class RegistroClienteForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
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
    email = EmailField("Email", validators=[
        Email()
    ])
    submit = SubmitField("Cadastrar")


class RegistroMotorForm(FlaskForm):

    equipamento = StringField("Equipamento", validators=[
        DataRequired("o campo é obrigatório")
    ])
    clientes = SelectField("Cliente", coerce=int)
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
        self.clientes.choices = [ 
            (clientes.id, clientes.name) for clientes in Clientes.query.all()
        ]


class RegistroAtividadeForm(FlaskForm):

    ordem_servico = StringField("Ordem de serviço", validators=[
        DataRequired("o campo é obrigatório")
    ])
    usuarios = SelectField("Técnico", coerce=int)
    clientes = SelectField("Cliente", coerce=int)
    motores = SelectField("Motor", coerce=int)
    status = SelectField("status", coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.usuarios.choices = [ 
                (usuarios.id, usuarios.name) for usuarios in Usuario.query.all()
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clientes.choices = [ 
            (clientes.id, clientes.name) for clientes in Clientes.query.all()
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.motores.choices = [ 
            (motores.id, motores.name) for motores in Motores.query.all()
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status.choices = ["Concluído", "Em Andamento", 'Encerrado"]
