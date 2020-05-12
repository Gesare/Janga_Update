import unittest
from app.models import Article
class ArticleTest(unittest.TestCase):
  '''
  test class to test behaviour of the article class
  '''
  def setUp(self):
    '''
    setup method that will run before every test
    '''
    self.new_article=Article("victor","floods","floods are raging","https://url","https://image","2020-05-08")
  def test_instance(self):
    '''
    test to assert whether new_article is an instance of the Article object
    '''
    self.assertTrue(isinstance(self.new_article,Article))