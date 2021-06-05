import os

class Config:
    """
    Config class the defines the config objects
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    NEWS_API_KEY =  os.environ.get('MOVIE_API_KEY')
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

    Debug = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}