from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
from app.forms import RegistroMotorForm
from app.models import Motores

from . import motores


#Tela de adicionar motores
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
        corrente.rpm = form.corrente.data
        db.session.add(motor)
        db.session.commit() 

        flash("Motor cadastrado com sucesso!", "success")
        return redirect(url_for(""))#adicionar rota correta
    return render_template("", form=form)#adicionar template correto

