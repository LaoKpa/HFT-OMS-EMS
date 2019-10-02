import sys
import os

ALPHA_VANTAGE = {
	"apikey": "Z853NF8RKPOWNK88",
	"url": "https://www.alphavantage.co/query"
}

LOGS_LOCATION = os.getenv('LOGS_LOCATION') or '/logs/'