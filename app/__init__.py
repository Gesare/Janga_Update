from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# from app.models import User

# create an application factory


def create_app(config_name):
    """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set the configurations
    app.config.from_object(config_options[config_name])

    # initialiaze the database
    db.init_app(app)

    # register your blueprints here
    from app.main import main
    from app.auth import auth
    

    app.register_blueprint(main)
    app.register_blueprint(auth)


    return app