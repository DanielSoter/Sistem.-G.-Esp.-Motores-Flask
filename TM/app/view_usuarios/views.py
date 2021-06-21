from flask import redirect, render_template, url_for
from flask_login import login_required
from app.forms import LoginForm, RegistroUsuarioForm, EdicaoUsuarioForm, RedefUsuarioForm
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import Usuario

from . import usuarios

@usuarios.route("/usuarios")
def tela_usuarios():
    usuarios = Usuario.query.all() # Select * from users; 
    return render_template("usuario.html", usuarios=usuarios)

@usuarios.route("/usuario/<int:id>", methods=["GET", "POST"])
def editar(id):
    usuarios = Usuario.query.get(id)
    form = EdicaoUsuarioForm()
    if form.validate_on_submit():
        usuarios.nome = form.nome.data
        usuarios.email = form.email.data
        usuarios.cargo = form.cargo.data
        print(usuarios.nome)
        db.session.commit()
        return redirect(url_for(".tela_usuarios"))
    form.nome.data = usuarios.nome
    form.email.data = usuarios.email
    form.cargo.data =usuarios.cargo
    return render_template("editar/editar_usuarios.html", form=form)


@usuarios.route("/usuario-redefinir/<int:id>", methods=["GET", "POST"])
def redefinir_senha(id):
    usuarios = Usuario.query.get(id)
    form = RedefUsuarioForm()
    if form.validate_on_submit():
        usuarios.senha = generate_password_hash(form.senha.data)
        print(usuarios.nome)
        db.session.commit()
        return redirect(url_for(".tela_usuarios"))
    return render_template("redef/redef_usuarios.html", form=form)


@usuarios.route("/cadastro-tecnico", methods=["GET", "POST"])
def regitro_tecnico():
    form = RegistroUsuarioForm()

    if form.validate_on_submit():
        usuario = Usuario()
        usuario.nome = form.nome.data
        usuario.email = form.email.data
        usuario.senha = generate_password_hash(form.senha.data)
        usuario.cargo = form.cargo.data

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for(".tela_usuarios"))
    return render_template("registro/registro_tecnico.html", form=form)

@usuarios.route("/técnico/delete/<int:id>")
def deletar_tecnico(id):
    usuarios = Usuario.query.filter_by(id=id).first()
    db.session.delete(usuarios)
    db.session.commit()

    return redirect(url_for(".tela_usuarios"))
      

    
