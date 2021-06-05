from flask import render_template
from . import main

@main.route('/')
def index():

    """return template and its contents"""
    name="1,2, app testing"

    return render_template('index.html', name = name)