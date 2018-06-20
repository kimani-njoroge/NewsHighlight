class Articles:
    def __init__(self, id, author, title, description, url, image, date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date


class Highlight:
    '''
    highlight class to define objects
    '''
    def __init__(self, id, name, category, url):
        self.id = id
        self.name = name
        self.category = category
        self.url = url