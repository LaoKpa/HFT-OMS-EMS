from HFTApp.scrapers import AlphaVantage

class ApplicationContext:

	application = None
	scrapers = {
		'alphavantage': AlphaVantage(),
	}

	def __init__(self, **config):
		for scraper in self.scrapers.values():
			scraper() # begin requesting from queue
	
	def add_request(self, scraper_name:str, key: str, value:dict):
		self.scrapers[scraper_name].put(key, value)

	def query_request(self, scraper_name, key):
		self.scrapers[scraper_name].query()