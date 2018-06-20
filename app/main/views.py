from flask import render_template
from . import main
from ..request import get_highlights, get_articles

# Views


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_articles = get_highlights('business')
    print(business_articles)
    tech = get_highlights('technology')
    ent = get_highlights('entertainment')
    title = 'NewsHighlights'
    # message = 'Welcome to news highlight'
    return render_template('index.html', title=title, business=business_articles, technology=tech, entertainment=ent)


@main.route('/templates/highlight/<id>')
def source(id):
    articles = get_articles(id)
    print(articles)
    return render_template('highlight.html', articles=articles)