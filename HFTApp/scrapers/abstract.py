import sys
import os
import logging
import asyncio

from HFTApp.settings import LOGS_LOCATION

class AbstractScraper:


	query_queue = {
		'_test_conn': {
			'endpoint': '',
			'query': ''
		},
	}

	started = {

	}

	"""

	"""
	default_timeout = 5 #ms

	def __init__(self):
		# setup logging
		self.log = logging.getLogger(__name__)

	def __call__(self, *args, **kwargs):
		return asyncio.run(self.execute(*args, **kwargs))

	async def execute(self):
		"""
		Start popping from queue
		"""
		task = asyncio.gather(*(self.get(**v) for v in self.query_queue.values()))
		# TODO figure out task structures
		yield task

	async def get(self, *args, **kwargs):
		raise NotImplementedError

	def put(self, *args, **kwargs):
		raise NotImplementedError

	def query(self):
		return self.started