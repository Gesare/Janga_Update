from flask import current_app
from flask_login import UserMixin
from . import db, login_manager
from _datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class Article:
    '''
    Article class to define article objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt

class User(db.Model, UserMixin):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    password = db.Column(db.String(60), nullable=False)
    
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Global:
  '''
  Global class to define global corona cases object
  '''
  def __init__(self,NewConfirmed,Totalconfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered):
    self.NewConfirmed=NewConfirmed
    self.Totalconfirmed=Totalconfirmed
    self.NewDeaths=NewDeaths
    self.TotalDeaths=TotalDeaths
    self.NewRecovered=NewRecovered
    self.TotalRecovered=TotalRecovered

class Countries:
  '''
  country class to define country objects
  '''
  def __init__(self,Country,NewConfirmed,Totalconfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered):
    self.Country=Country
    self.NewConfirmed=NewConfirmed
    self.Totalconfirmed=Totalconfirmed
    self.NewDeaths=NewDeaths
    self.TotalDeaths=TotalDeaths
    self.NewRecovered=NewRecovered
    self.TotalRecovered=TotalRecovered