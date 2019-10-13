import flask
import json
from HFTApp.extensions import logger, app

api = flask.Flask(__name__)

@api.route('/')
def index():
	return "connected"

@api.route('/{scraper_name}', method="GET")
def scrapers(scraper_name:str, params:dict):
	return app.add_request(scraper_name, key=f"{params['endpoint']}.{params['function']}", value=params)