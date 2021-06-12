from app.autenticacao import autenticacao as autenticacao_blueprint
from app.usuarios import usuarios as usuarios_blueprint
from app.motores import motores as motores_blueprint
from app.clientes import clientes as clientes_blueprint
from app.atividades import atividades as atividades_blueprint


def init_app(app):
    app.register_blueprint(autenticacao_blueprint)
    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(motores_blueprint)
    app.register_blueprint(clientes_blueprint)
    app.register_blueprint(atividades_blueprint)
    
