import urllib.request,json
from .models import Article,Countries

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

def get_country():
  '''
  function that returns json response to url request
  '''
  get_country_url=corona_url
  print(get_country_url)
  with urllib.request.urlopen(get_country_url) as url:
    get_country_data=url.read()
    get_country_response= json.loads(get_country_data)

    country_results=None
    if get_country_response['Countries']:
      country_results_list = get_country_response['Countries']
      country_results = process_country(country_results_list)
  return country_results

def process_country(country_list):
  '''
  Function  that processes the  country result and transform them to a list of Objects

  '''
  country_results = []
  for country_item in country_list:
    Country = country_item.get('Country')
    TotalConfirmed = country_item.get('TotalConfirmed')
    TotalDeaths = country_item.get('TotalDeaths')      
    TotalRecovered = country_item.get('TotalRecovered')

    if Country:
      country_object = Countries(Country,TotalConfirmed,TotalDeaths,TotalRecovered)
      country_results.append(country_object)

  return country_results
