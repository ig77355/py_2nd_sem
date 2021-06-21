'''import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
import lxml
from lxml import html
from datetime import datetime, timedelta
import time
'''

url = 'http://finance.yahoo.com/quote/%5EIXIC/history?&interval=1d'
data = pd.read_html(url, flavor='bs4', header=0, encoding='UTF-8')
response = requests.get(url)
print(response)