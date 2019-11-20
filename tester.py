import urllib.request
from builtins import print

import mechanize
import requests
from bs4 import BeautifulSoup

common = ['/item/5', '/item/88', '/item/93', '/item/96', '/item/99', '/item/107', '/item/109', '/item/120', '/item/126', '/item/139', '/item/163', '/item/165', '/item/172', '/item/173', '/item/176', '/item/186', '/item/370', '/item/451', '/item/960']
url = 'https://crossoutdb.com/item/5'

response = requests.get(url)

# parse html
crossoutdb_page = BeautifulSoup(response.content, 'html.parser')

material = crossoutdb_page.find_all('a', style="font-weight: bold;")[0].text.strip()
amount = crossoutdb_page.find_all('div', class_="label-md pull-left")[0].text.strip()
print(material, amount)
input()
