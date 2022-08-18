from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskconf import SELECTED_CONFIG


db = SQLAlchemy()


def create_app(flask_configuration=SELECTED_CONFIG):
    app = Flask(__name__)
    app.config.from_object(flask_configuration)

    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models
