from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
from app.forms import RegistroMotorForm, EditarMotorForm
from app.models import Motores

from . import motores


@motores.route("/motores")
def tela_motor():
    motores = Motores.query.all() 
    return render_template("motores.html", motores=motores)


@motores.route("/motor/cadastrar", methods=["GET", "POST"])
def cadastrar_motor():
    form = RegistroMotorForm()

    if form.validate_on_submit():
        motor = Motores()
        motor.equipamento = form.equipamento.data
        motor.cliente = form.cliente.data
        motor.marca = form.marca.data
        motor.modelo = form.modelo.data
        motor.ip = form.ip.data
        motor.cv = form.cv.data
        motor.rpm = form.rpm.data
        motor.corrente = form.corrente.data
        #corrente.rpm = form.corrente.data
        db.session.add(motor)
        db.session.commit() 

        flash("Motor cadastrado com sucesso!", "success")
        return redirect(url_for(".tela_motor"))
    return render_template("registro/registro_motores.html", form=form)


@motores.route("/motor/<int:id>", methods=["GET", "POST"])
def editar(id):
    motores = Motores.query.get(id)
    form = EditarMotorForm()
    if form.validate_on_submit():
        motores.equipamento = form.equipamento.data
        motores.cliente = form.cliente.data
        motores.marca = form.marca.data
        motores.modelo = form.modelo.data
        motores.ip = form.ip.data
        motores.cv = form.cv.data
        motores.rpm = form.rpm.data
        motores.corrente = form.corrente.data
        db.session.commit()
        return redirect(url_for(".tela_motor"))
    form.equipamento.data = motores.equipamento
    form.cliente.data = motores.cliente
    form.marca.data = motores.marca
    form.modelo.data = motores.modelo
    form.ip.data = motores.ip
    form.cv.data = motores.cv
    form.rpm.data = motores.rpm
    form.corrente.data = motores.corrente

    return render_template("editar/editar_motores.html", form=form)

@motores.route("/motor/delete/<int:id>")
def deletar(id):
    motores = Motores.query.filter_by(id=id).first()
    db.session.delete(motores)
    db.session.commit()

    return redirect(url_for(".tela_motor"))