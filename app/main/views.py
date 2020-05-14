
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_article
from ..models import Article

#views
@main.route('/')
def index():
  '''
  view root that returns the index page and various news sources 
  '''
  return render_template('index.html')

@main.route('/international')
def articles():
  '''
  view articles that returns various disaster articles from vaious sites
  '''
  articles=get_article()
  title = f'NH | {id}'

  return render_template('News/articles.html',articles=articles)

@main.route("/about")
def about():
    pass
