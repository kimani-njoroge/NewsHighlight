import urllib.request, json
from .models import Highlight
from .models import Articles


api_key = None
base_url = None
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


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


def process_results(highlight_results_list):
    '''
    process highlight result and transform to list of object
    :param highlight_results_list:
    :return:
    '''
    highlight_results = []
    for highlight_cont in highlight_results_list:
        id = highlight_cont.get('id')
        name = highlight_cont.get('name')
        category = highlight_cont.get('category')
        url = highlight_cont.get('url')

        highlight_object = Highlight(id, name, category, url)
        highlight_results.append(highlight_object)
    return highlight_results


def get_articles(id):
    get_articles_url = articles_url.format(id, api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results = get_articles_response['articles']
            articles_results = process_articles(articles_results)

    return articles_results

    #     articles_results = json.loads(url.read())
    #     articles_object = None
    #     if articles_results['articles']:
    #         articles_object = process_articles(articles_results['articles'])
    #
    # return articles_object


def process_articles(articles_list):
    articles_results = []

    for article_cont in articles_list:
        id = article_cont.get('id')
        author = article_cont.get('author')
        title = article_cont.get('title')
        description = article_cont.get('description')
        url = article_cont.get('url')
        image = article_cont.get('urlToImage')
        date = article_cont.get('publishedAt')
        articles_object = Articles(id,author,title,description,url,image,date)
        articles_results.append(articles_object)

    return articles_results
