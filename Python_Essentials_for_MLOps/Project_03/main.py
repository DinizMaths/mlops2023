import os
import sys
import requests
import logging

from utils import *

import pandas as pd

sys.dont_write_bytecode = True


DATA_URL = "https://dsserver-prod-resources-1.s3.amazonaws.com/764/fires.csv"

logging.basicConfig(filename="main.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logging.getLogger("urllib3").setLevel(logging.WARNING)

download_csv(DATA_URL, "./data/fires.csv")

data = pd.read_csv("./data/fires.csv")