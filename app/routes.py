from bs4 import BeautifulSoup
from flask import Blueprint, request
from dotenv import load_dotenv
import requests



load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)


def is_dinosaur(search_term):
    dino = {"answer" : "no"}
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
        return {"answer" : "no"}

    infobox = soup.find('table',{'class':'infobox','class':'biota'})

    if infobox:
        dinosaur = infobox.find(href="/wiki/Dinosaur")
        if dinosaur:
            dino = {"answer" : "yes"}

    return dino


@proxy_bp.route("/search", methods=["GET"])
def return_hello():

    critter_query = request.args.get("subject")

    return is_dinosaur(critter_query)

