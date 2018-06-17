from app import app
import urllib.request, json
from models import highlight

Highlight = highlight.Highlight

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_highlights(category):
    '''
    function to get json response of out request
    :param category
    :return:
    '''

    get_highlights_url = base_url.format(category, api_key)
    print(get_highlights_url)
    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        highlight_results = None

        if get_highlights_response['sources']:
            highlight_results = get_highlights_response['sources']
            highlight_results = process_results(highlight_results)

    return highlight_results