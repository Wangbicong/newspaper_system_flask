from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    app.config.from_pyfile('..\\instance\\config.py')

    db.init_app(app)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

