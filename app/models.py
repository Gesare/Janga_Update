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

