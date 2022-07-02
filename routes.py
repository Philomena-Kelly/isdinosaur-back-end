from requests import get
from flask import Blueprint, Flask
from bs4 import BeautifulSoup
from flask import Flask
import requests



app = Flask(__name__)
SITE_NAME = 'https://google.com/'

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def proxy(path):

# dinosaur = Blueprint("goals_bp", __name__, url_prefix="/goals")

def is_dinosaur(search_term):
    dino = "no"
    url = 'https://en.wikipedia.org/w/api.php'

    params = {
                'action':'parse',
                'prop':'text',
                'format':'json',
                'page':search_term,
                'section':0,
                'redirects':''
            }

    data = requests.get(url, params=params).json()
    try:
        soup = BeautifulSoup(data['parse']['text']['*'],'html.parser')
    except:
        return "no"

    infobox = soup.find('table',{'class':'infobox','class':'biota'})

    if infobox:
        dinosaur = infobox.find(href="/wiki/Dinosaur")
        if dinosaur:
            dino = "yes"

    return dino


@app.route("/search", methods=["GET"])
def return_hello():

    return is_dinosaur("Brontosaurus")  

