from flask import render_template,request
from . import main
from ..models import Newsource
from ..request import get_news

@main.route('/')
def index():

    """return template and its contents"""
    name="1,2, app testing"
    news_sources = get_news("everything")
    results = get_news("top-headlines")

    return render_template('index.html', name = name, sources=news_sources, feeds=results)



