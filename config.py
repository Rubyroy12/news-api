import os

class Config:
    """
    Config class the defines the config objects
    #top-headlines
    #sources
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?q=tesla&from=2021-05-06&sortBy=publishedAt&apiKey={}'
    NEWS_API_KEY =  os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    """
    production classfor deployent 
    """

    pass

class DevConfig(Config):
    """
    development class for development 
    """

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}