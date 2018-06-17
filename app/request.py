from app import app
import urllib.request, json
from models import highlight

Highlight = highlight.Highlight

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]