import os

class Config:
  '''
  General configuration parent class
  '''
  BASE_URL='https://newsapi.org/v2/everything?q=floods&earthquakes&landslides&volcano-eruption&apiKey={}'
  API_KEY=os.environ.get('API_KEY')
  SECRET_KEY = os.environ.get("SECRET_KEY")
  CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
  

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
  DEBUG = True
  
  

class TestingConfig(Config):
    TESTING = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'testing':TestingConfig, 
}  



