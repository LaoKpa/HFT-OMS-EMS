import sys
import os
import requests
import json

from .abstract import AbstractScraper
from HFTApp.settings import ALPHA_VANTAGE

class AlphaVantage(AbstractScraper):
	_required_params = [
		"apikey"
	]
	def __init__(self, config:dict=None):
		self.config = config or ALPHA_VANTAGE
		self.url:str = self.config.pop('url')
		
		# self.header = """{

		# }""".format(**{k:v for k, v in config.items() if k in self._required_params})

		super().__init__()


	async def get(self, query:dict, endpoint=""):
		"""
		Queries alphavantage
		"""
		_query = json.dumps(
			[query.setdefault(key, self.config[key]) for key in self._required_params]
		)		
		
		yield requests.get("{self.url}/{endpoint}", params=_query, stream=True)

	def put(self, key:str, value:dict={}):
		"""
		Adds to queue to be queried
		"""
		self.query_queue[key]=value
		return (key,len(self.query_queue))