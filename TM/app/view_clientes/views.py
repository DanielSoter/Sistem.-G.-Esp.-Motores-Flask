from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
from app.forms import RegistroClienteForm, EditarClienteForm
from app.models import Clientes, Motores

from . import clientes

@clientes.route("/clientes")
def tela_cliente():
    clientes = Clientes.query.all() 
    return render_template("clientes.html", clientes=clientes)


#Tela de adicionar clientes
@clientes.route("/clientes/cadastrar", methods=["GET", "POST"])
def cadastrar_cliente():
    form = RegistroClienteForm()

    if form.validate_on_submit():
        cliente = Clientes()
        cliente.nome = form.nome.data
        cliente.email = form.email.data
        cliente.cpf = form.cpf.data
        cliente.endereco = form.endereco.data
        cliente.telefone = form.telefone.data
        db.session.add(cliente)
        db.session.commit() 

        flash("Cliente cadastrado com sucesso!", "success")
        return redirect(url_for(".tela_cliente"))#adicionar rota correta
    return render_template("registro/registro_clientes.html", form=form)


@clientes.route("/cliente/<int:id>", methods=["GET", "POST"])
def editar(id):
    clientes = Clientes.query.get(id)
    form = EditarClienteForm()
    if form.validate_on_submit():
        clientes.nome = form.nome.data
        clientes.email = form.email.data
        clientes.cpf = form.cpf.data
        clientes.endereco = form.endereco.data
        clientes.telefone = form.telefone.data
        db.session.commit()
        return redirect(url_for(".tela_cliente"))
    form.nome.data = clientes.nome 
    form.email.data = clientes.email
    form.cpf.data = clientes.cpf
    form.endereco.data = clientes.endereco 
    form.telefone.data = clientes.telefone
    return render_template("editar/editar_clientes.html", form=form)


@clientes.route("/cliente/delete/<int:id>")
def deletar(id):
    clientes = Clientes.query.filter_by(id=id).first()
    db.session.delete(clientes)
    db.session.commit()

    return redirect(url_for(".tela_cliente"))

@clientes.route("/cliente/<int:id>")
def unique(id):
        motores = Motores.query.get(id)
        return render_template("unique/unique_cliente.html", clientes=motores)