import unittest
from app.models import Global
class GlobalTest(unittest.TestCase):
  '''
  test class to test behaviour of the Global class
  '''
  def setUp(self):
    '''
    setup method that will run before every test
    '''
    self.new_global=Global(10,10,10,10,10,10)
  def test_instance(self):
    '''
    test to assert whether new_global is an instance of the Global object
    '''
    self.assertTrue(isinstance(self.new_global,Global))