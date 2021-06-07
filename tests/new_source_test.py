import unittest
from app.models import Newsource

class New_source_Test(unittest.TestCase):
    """Test method to test the behaviour of Newsource class"""
    def setUp(self):
        """SetUp method that can be run before everytests"""
        self.news_source = Newsource('ABC_news','Terror attack','Texas attorney is under fire over racist comment on Asian Tesla employees LinkedIn post','https://images.unsplash.com/photo-1600585154166-d8897c8f930d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8ODB8fGRlc2lnbiUyMHRoaW5raW5nfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60','2021-06-06T22:01:48Z','http://techcrunch.com/2021/06/06/elon-musk-officially-hits-the-brakes-on-tesla-model-s-plaid/')
    
    def test_instance_(self):
        """Test"""

        self.assertTrue(isinstance(self.new_source,Newsource))


