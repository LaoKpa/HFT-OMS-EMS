import sys
import os
import requests

from .abstract import AbstractScraper
from HFTApp.settings import ALPHA_VANTAGE

class AlphaVantage(AbstractScraper):

	def __init__(self, config):
		self.config = config or ALPHA_VANTAGE
		self.url = self.config.pop("url")
		super().__init__()


	def get(self, query):
		"""
		Queries alphavantage
		"""
		requests.get(self.url)

		