from flask import render_template
from app import app
# from .request import get_highlights

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # business_articles = get_highlights('business')
    # print(business_articles)
    # technology = get_highlights('technology')
    # entertainment = get_highlights('entertainment')
    title = 'NewsHighlights'
    # message = 'Welcome to news highlight'
    return render_template('index.html') #title=title, business=business_articles)