import os

class Config:
  '''
  General configuration parent class
  '''
  BASE_URL='https://newsapi.org/v2/everything?q=floods&earthquakes&landslides&volcano-eruption&apiKey={}'
  API_KEY=os.environ.get('API_KEY')
  SECRET_KEY = os.environ.get("SECRET_KEY")
  CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jerome:1234@localhost/blog'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
  

class ProdConfig(Config):
  '''
  Production  configuration child class
  Args:
  Config: The parent configuration class with General configuration settings
  '''
  pass
  
  
class DevConfig(Config):
  '''
  Development  configuration child class
  Args:
  Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jerome:1234@localhost/blog'
  DEBUG = True

class TestingConfig(Config):
    TESTING = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'testing':TestingConfig, 
}  



