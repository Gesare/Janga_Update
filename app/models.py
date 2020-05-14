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

class Country:
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