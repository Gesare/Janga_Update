from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

bootstrap=Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()
mail = Mail()

def create_app(config_name):
  """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """
  
  app = Flask(__name__)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  #creating app configurations
  app.config.from_object(config_options[config_name])
  #initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  bcrypt.init_app(app)
  mail.init_app(app)
  #blueprint register
  from app.main import main
  from app.auth import auth
  
  app.register_blueprint(main)
  app.register_blueprint(auth)
  #setting config
  from .request import configure_request
  configure_request(app)

  return app