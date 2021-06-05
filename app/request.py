import urllib.request,json
from .models import Newsource

api_key= None

base_url= None

def configure_request(app):
    """Config"""
    global base_url,api_key
    base_url=app.config['NEWS_API_BASE_URL']
    api_key= app.config['NEWS_API_KEY']


def get_news(category):
    """Get news"""
    get_news_url= base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response ["articles"]:
            news_results_list=get_news_response["articles"]
            news_results= process_results(news_results_list)

    return news_results

def process_results(new_list):
    """Process"""
    news_results=[]
    for news_items in new_list:
        id=news_items.get('id')
        name= news_items.get('name')
        desciption= news_items.get('desciption')

        if desciption:
            news_object=Newsource(id, desciption, category)
            news_results.append(news_object)
    print(news_results)
    return news_results
    


