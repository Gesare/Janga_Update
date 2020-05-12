import urllib.request,json
from .models import Article

apikey=None
base_url=None

def configure_request(app):
  '''
  function to make url and apikey available globally
  '''
  apikey=app.config['API_KEY']
  base_url=app.config['BASE_URL']

def get_article():
  '''
  function that returns json response to url request
  '''
  get_article_url=base_url.format(apikey) 
  print(get_article_url)
  with urllib.request.urlopen(get_article_url) as url:
    get_article_data=url.read()
    get_article_response= json.loads(get_article_data)

    article_results=None
    if get_article_response['articles']:
      article_results_list = get_article_response['articles']
      article_results = process_results(article_results_list)
  return article_results
  
def process_results(article_list):
