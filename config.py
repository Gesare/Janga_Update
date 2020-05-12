import os
class Config:
  '''
  General configuration parent class
  '''
  BASE_URL='https://newsapi.org/v2/everything?q=natural-disaster&apiKey={}'
  API_KEY=os.environ.get('API_KEY')
  
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
config_options = {
'development':DevConfig,
'production':ProdConfig
}  