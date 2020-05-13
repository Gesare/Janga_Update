from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
  '''
  creates an instances of the application 
  and passes the config name, i.e development
  or production, the will then pick the environments
  from the configuration classes in config
  '''
  
  app = Flask(__name__)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)

  #blueprint register
  from app.main import main
  from app.auth import auth
  
  app.register_blueprint(main)
  app.register_blueprint(auth)
  #setting config
  from .request import configure_request
  configure_request(app)

  return app
