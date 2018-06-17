from flask import render_template
from app import app
from .request import get_highlights,get_articles

# Views
@app.route('/')
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

app.route('/sources/<int:id>')
def articles(id):
    articles = get_articles(id)
    return render_template('highlight.html', articles=articles)