import unittest
from app.models import Countries
class CountryTest(unittest.TestCase):
  '''
  test class to test behaviour of the country class
  '''
  def setUp(self):
    '''
    setup method that will run before every test
    '''
    self.new_country=Countries("Kenya",10,10,10,10,10,10)
  def test_instance(self):
    '''
    test to assert whether new_country is an instance of the Countries object
    '''
    self.assertTrue(isinstance(self.new_country,Countries))