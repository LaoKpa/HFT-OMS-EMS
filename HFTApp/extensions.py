import logging
import sys
import os
import HFTApp
from HFTApp.settings import LOGS_LOCATION
from HFTApp.main import ApplicationContext
from HFTApp.api import api as APIContext

logger = logging.getLogger(f"HFTApp_{os.getenv('BUILD_TS')}")
app = ApplicationContext()
api = APIContext