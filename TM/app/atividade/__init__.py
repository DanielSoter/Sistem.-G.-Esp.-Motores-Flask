from flask import Blueprint

atividades = Blueprint("atividades", __name__)

from . import views