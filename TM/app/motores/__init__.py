from flask import Blueprint

motores = Blueprint("motores", __name__)

from . import views