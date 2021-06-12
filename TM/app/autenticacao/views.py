from datetime import timedelta

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.forms import LoginForm, RegistroUsuarioForm
from app.models import Usuario

from . import autenticacao

#Usuario.index está correto? devo redireciona-lo para essa rota?
#A rota está correta?
@autenticacao.route("/register", methods=["GET", "POST"])
def register():
    form = RegistroUsuarioForm()

    if form.validate_on_submit():
        usuario = Usuario()
        usuario.nome = form.nome.data
        usuario.email = form.email.data
        usuario.senha = generate_password_hash(form.senha.data)
        usuario.cargo = form.cargo.data

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for("usuarios.home"))
    return render_template("registro.html", form=form)

#login
@autenticacao.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if not usuario:
            flash("Credênciais incorretas", "danger")
            return redirect(url_for(".index"))

        if not check_password_hash(usuario.senha, form.senha.data):
            flash("Credênciais incorretas", "danger")
            return redirect(url_for(".index"))

        login_user(usuario, remember=form.remember.data, duration=timedelta(days=7))
        return redirect(url_for("usuarios.home"))

    return render_template("login.html", form=form)


#o correto é user.index ou usuario.index?
@autenticacao.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".index"))

