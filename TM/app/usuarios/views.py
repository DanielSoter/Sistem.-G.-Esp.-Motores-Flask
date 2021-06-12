from flask import redirect, render_template, url_for
from flask_login import login_required

from app import db
from app.models import Usuario

from . import usuarios

@usuarios.route("/pagina-inicial")
def home():
    usuarios = Usuario.query.all() # Select * from users; 
    return render_template("usuarios.html", usuarios=usuarios)

@usuarios.route("/usuario/<int:id>")
def unique(id):
    usuarios = Usuario.query.get(id)
    return render_template("usuario.html", usuarios=usuarios)
