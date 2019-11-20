import urllib.request
import mechanize
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36", "Content-Type": "text/html; charset=utf-8"}
common = ['/item/5', '/item/88', '/item/93', '/item/96', '/item/99', '/item/107', '/item/109', '/item/120', '/item/126', '/item/139', '/item/163', '/item/165', '/item/172', '/item/173', '/item/176', '/item/186', '/item/370', '/item/451', '/item/960']
url = 'https://crossoutdb.com/item/960'


response = urllib.request.urlopen(url).read()
br = mechanize.Browser()
resp = br.open(url)
print(resp.info())  # headers
print(resp.read())  # content

# response = requests.get(url, headers=header, verify=False)

# parse html
crossoutdb_page = BeautifulSoup(response.content, 'html.parser')
crossoutdb_page.find_all('tr', class_='recipe-part')
