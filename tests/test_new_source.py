import unittest
from app.models import Newsource

class New_source_Test(unittest.TestCase):
    """Test method to test the behaviour of Newsource class"""
    def setUp(self):
        """SetUp method that can be run before everytests"""
        self.news_source = Newsource('ABC_news','Terror attack','Texas attorney','https://images.unsplash.com/','test-time','test_url')
        # self.new_source = Newsource('Test author','Test title','Test description','Test url','Test image','Test publishedAt')

    def test_instance(self):
        """Test"""

        self.assertTrue(isinstance(self.news_source,Newsource))


