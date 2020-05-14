import urllib.request,json
from .models import Article,Countries,Global

apikey=None
base_url=None
corona_url=None

def configure_request(app):
  '''
  function to make url and apikey available globally
  '''
  global apikey,base_url,corona_url
  apikey=app.config['API_KEY']
  base_url=app.config['BASE_URL']
  corona_url=app.config['CORONA_URL']

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
  '''
  Function  that processes the article result and transform them to a list of Objects

  Args:
    article: A list of dictionaries that contain article details

  Returns :
    article_results: A list of movie objects
  '''
  article_results = []
  for article_item in article_list:
    author=article_item.get('author')
    title= article_item.get('title')
    description = article_item.get('description')
    url=article_item.get('url')
    urlToImage= article_item.get('urlToImage')
    publishedAt= article_item.get('publishedAt')
    
    if urlToImage:
      article_object = Article(author,title,description,url,urlToImage,publishedAt)
      article_results.append(article_object)
  return article_results

def get_global():
  '''
  function that returns json response for global corona statistics
  '''
  get_global_url=corona_url
  print(get_global_url)
  with urllib.request.urlopen(get_global_url) as url:
    global_data = url.read()
    global_response = json.loads(global_data)

    global_result = None

    if quote_response:
      author = quote_response.get('author')
      quote = quote_response.get('quote')
            

      quote_result = Quote(author, quote)

    return quote_result


