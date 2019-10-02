import sys
import os
import logging

from HFTApp.settings import LOGS_LOCATION

class AbstractScraper:

	def __init__(self):
		# setup logging
		self.log = logging.getLogger(__name__)

	def __call__(self, *args, **kwargs):
		return self.execute(*args, **kwargs)

	def execute(self):
		raise NotImplementedError