# get the HTML
import html
from bs4 import BeautifulSoup
import requests

import pandas as pd
import json
response = requests.get("https://www.daraz.pk/")

# parsing (beautifying the content)
soup = BeautifulSoup(response.text, 'html')
data=soup.findAll(["h1","h2","h3", "a"])

# HTML tree traversal (retreiving/scraping specific data from HTML)
for tags in data:
     alltags=tags.text.strip()
     print(tags.name + ' -> ' + alltags) 
     