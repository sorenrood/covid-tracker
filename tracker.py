# Imports
from bs4 import BeautifulSoup
import requests
import json
from lxml import html
import sys

# Constant URL that we scrape
url = 'https://spu.edu/administration/health-services/covid-19-cases'

# Setup for lxml
page = requests.get(url)
tree = html.fromstring(page.content)

# Use these lists to store data
cases = []
dates = []

# This is the path to the div that stores the updated data
path_to_cases = '//*[@id="pageBody"]/div/p/text()'
path_to_dates = '//*[@id="pageBody"]/div/strong/text()'

# Get cases and add to cases list
for element in tree.xpath(path_to_cases):
    cases.append(element)

# Get dates and append to dates list
for element in tree.xpath(path_to_dates):
    dates.append(element)

# Check to make sure length is the same for both lists
if len(cases) != len(dates):
    sys.exit('The cases list is not the same length as the dates list. Something went wrong with parsing.')

# Store the number of cases
number_of_cases = len(cases)

# Output
for x in range(0,number_of_cases):
    print('{}: {}'.format(dates[x], cases[x]))
