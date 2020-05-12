import os

class Config:
  '''
  General configuration parent class
  '''
  BASE_URL='https://newsapi.org/v2/everything?q=floods&earthquakes&landslides&volcano-eruption&apiKey={}'
  API_KEY=os.environ.get('API_KEY')
  SECRET_KEY = os.environ.get("SECRET_KEY")
  CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProdConfig(Config):
  '''
  Production  configuration child class
  Args:
  Config: The parent configuration class with General configuration settings
  '''
  DEBUG = os.environ.get("DEBUG")
  
class DevConfig(Config):
  '''
  Development  configuration child class
  Args:
  Config: The parent configuration class with General configuration settings
  '''

  DEBUG = os.environ.get("DEBUG")

class TestingConfig(Config):
    TESTING = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'testing':TestingConfig, 
}  



