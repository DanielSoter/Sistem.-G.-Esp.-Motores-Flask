from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
from app.forms import RegistroAtividadeForm
from app.models import Atividade

from . import atividades


#Tela de adicionar atividades
@atividades.route("/atividade/cadastrar", methods=["GET", "POST"])
def cadastrar_atividade():
    form = RegistroAtividadeForm()

    if form.validate_on_submit():
        atividade = Atividade()
        atividade.ordem_servico = form.ordem_servico.data
        atividade.cliente = form.cliente.data
        atividade.motor = form.motor.data
        atividade.usuario = form.usuario.data
        db.session.add(atividade)
        db.session.commit() 

        flash("Atividade cadastrada com sucesso!", "success")
        return redirect(url_for(""))#adicionar rota correta
    return render_template("", form=form)#adicionar template correto

