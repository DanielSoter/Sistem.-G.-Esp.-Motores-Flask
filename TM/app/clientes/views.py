from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
from app.forms import RegistroClienteForm
from app.models import Clientes

from . import clientes


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
        return redirect(url_for(""))#adicionar rota correta
    return render_template("", form=form)#adicionar template correto