from flask import render_template,request
from . import main
from ..models import Newsource
from ..request import get_news

@main.route('/')
def index():

    """return template and its contents"""
    name="1,2, app testing"
    news_sources = get_news("everything")

    return render_template('index.html', name = name, sources=news_sources)

@main.route('/tesla')
def articles():
    """return"""
    news_sources = get_news("sources")
    
    return render_template('article.html', name = name, sources=news_sources)


