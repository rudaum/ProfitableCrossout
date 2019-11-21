from builtins import print

import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

common = ['/item/5', '/item/830', '/item/865', '/item/93', '/item/96', '/item/99', '/item/107', '/item/109', '/item/120', '/item/126',
          '/item/139', '/item/163', '/item/165', '/item/172', '/item/173', '/item/176', '/item/186', '/item/370',
          '/item/451', '/item/960']
prx_user = 'rudolf.wolter'
prx_pwd = 'C3t3d3s3!'
proxies = {
    "http": "http://{}:{}@kn.proxy.int.kn:80".format(prx_user, prx_pwd),
    "https": "http://{}:{}@kn.proxy.int.kn:80".format(prx_user, prx_pwd)
}


def get_craft_materials(uid):
    url = 'https://crossoutdb.com/{}'.format(uid)
    craft_materials = OrderedDict()
    response = requests.get(url, proxies=proxies, verify=False)
    # parse html
    item_page = BeautifulSoup(response.content, 'html.parser')
    for row in item_page.findAll('tr', class_="depth-1"):
        if row.attrs['data-parentuniqueid'] == '0':
            material = row.find('a', style="font-weight: bold;").text.strip()
            amount = row.find('div', class_="label-md pull-left").text.strip().split()[0]
            # unit_value = row.find('div', class_="recipe-price label-md rec-right").text.strip().split()[0]
            craft_materials[material] = amount
    return craft_materials


x = get_craft_materials(common[1])
for k, v in x.items():
    print('Material: {} / Ammount: {}'.format(k, v))