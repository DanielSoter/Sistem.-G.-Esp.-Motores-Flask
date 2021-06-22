from flask import flash, redirect, render_template, url_for
from flask_login import current_user
from datetime import datetime
from app import db
from app.forms import RegistroAtividadeForm, EditarAtividadeForm, RelatorioAtividadeForm
from app.models import Atividade

from . import atividades


@atividades.route("/pagina-inicial")
def home():
    atividades = Atividade.query.all()
    return render_template("atividade.html", atividades=atividades)


@atividades.route("/atividade/cadastrar", methods=["GET", "POST"])
def cadastrar_atividade():
    form = RegistroAtividadeForm()

    if form.validate_on_submit():
        atividade = Atividade()
        atividade.ordem_servico = form.ordem_servico.data
        atividade.cliente = form.cliente.data
        atividade.motor = form.motor.data
        atividade.usuario = form.usuario.data
        atividade.data_inicio = form.data_inicio.data
        atividade.status = form.status.data
        atividade.data_fim = form.data_fim.data
        atividade.conclusao = form.conclusao.data
        db.session.add(atividade)
        db.session.commit() 

        flash("Atividade cadastrada com sucesso!", "success")
        return redirect(url_for(".home"))#adicionar rota correta
    return render_template("registro/registro_atividades.html", form=form)#adicionar template correto


@atividades.route("/atividade/<int:id>", methods=["GET", "POST"])
def editar(id):
    atividade = Atividade.query.get(id)
    form = EditarAtividadeForm()
    if form.validate_on_submit():
        atividade.ordem_servico = form.ordem_servico.data
        atividade.cliente = form.cliente.data
        atividade.motor = form.motor.data
        atividade.usuario = form.usuario.data
        atividade.data_inicio = form.data_inicio.data
        atividade.status = form.status.data
        atividade.data_fim = form.data_fim.data
        atividade.conclusao = form.conclusao.data
        db.session.commit()
        return redirect(url_for(".home"))
    form.ordem_servico.data = atividade.ordem_servico
    form.cliente.data = atividade.cliente
    form.motor.data = atividade.motor
    form.usuario.data = atividade.usuario
    form.data_inicio.data = atividade.data_inicio
    form.status.data = atividade.status
    form.data_fim.data = atividade.data_fim
    form.conclusao.data = atividade.conclusao
    return render_template("editar/editar_atividade.html", form=form)


@atividades.route("/atividade/ralatorio/<int:id>", methods=["GET", "POST"])
def relatorio(id):
    atividade = Atividade.query.get(id)
    form = RelatorioAtividadeForm()
    form.ordem_servico.data = atividade.ordem_servico
    form.cliente.data = atividade.cliente
    form.motor.data = atividade.motor
    form.usuario.data = atividade.usuario
    form.data_inicio.data = atividade.data_inicio.strftime('%d/%m/%Y')
    form.status.data = atividade.status
    form.data_fim.data = atividade.data_fim.strftime('%d/%m/%Y')
    form.conclusao.data = atividade.conclusao
    return render_template("relatorio.html", form=form)


@atividades.route("/atividade/delete/<int:id>")
def deletar(id):
    atividade = Atividade.query.filter_by(id=id).first()
    db.session.delete(atividade)
    db.session.commit()

    return redirect(url_for(".home"))
      