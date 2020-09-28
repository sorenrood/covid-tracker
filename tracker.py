# Imports
from bs4 import BeautifulSoup
import requests
import json
from lxml import html

# Constant URL that we scrape
url = 'https://spu.edu/administration/health-services/covid-19-cases'

# Setup for lxml
page = requests.get(url)
tree = html.fromstring(page.content)

# Use these lists to store data
cases = []
dates = []

# Loop to fetch data
for i in range(1, 10):
    object = tree.xpath('//*[@id="pageBody"]/div/p[{}]/text()'.format(i))
    cases.append(object)

# Output
for case in cases:
    print(case)
