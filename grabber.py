import requests
import json
from bs4 import BeautifulSoup
from classes import Resource, CommonCraftable, RareCraftable, EpicCraftable, LegendaryCraftable, RelicCraftable
from settings import *

def get_craft_materials(uid):
    url_ = 'https://crossoutdb.com/{}'.format(uid)
    craft_materials = {}
    response_ = requests.get(url_, proxies=proxies, verify=False)
    # parse html
    item_page = BeautifulSoup(response_.content, 'html.parser')
    for row in item_page.findAll('tr', class_="depth-1"):
        if row.attrs['data-parentuniqueid'] == '0':
            material = row.find('a', style="font-weight: bold;").text.strip()
            amount = row.find('div', class_="label-md pull-left").text.strip().split()[0]
            # unit_value = row.find('div', class_="recipe-price label-md rec-right").text.strip().split()[0]
            craft_materials[material] = amount
    return craft_materials


# Setting and emptying the Data Files
open(resources_file, 'w').close()
open(dict_resources, 'w').close()
open(craftables_file, 'w').close()
open(dict_commons, 'w').close()
open(dict_rares, 'w').close()
open(dict_epics, 'w').close()
open(dict_legendaries, 'w').close()
open(dict_relics, 'w').close()

# CrossoutDB Main Page
url = 'https://crossoutdb.com/#length=-1.'
response = requests.get(url, proxies=proxies, verify=False)

# parse html
crossoutdb_page = BeautifulSoup(response.content, 'html.parser')
# crossoutdb_page = BeautifulSoup(open("html/page.html", encoding="utf8"), 'html.parser')

# Grabbing Items
for table_row in crossoutdb_page.find_all('tr', class_='selected-row'):
    item_id = table_row.find('a')['href'].strip()
    item_name = table_row.find('h4', class_="item-title").text.strip()
    item_rarity = table_row.find('span').text.strip()
    item_faction = table_row.find_all('div', class_='label-md-left')[0].text.strip()
    item_type = table_row.find_all('div', class_='label-md-left')[2].text.strip()
    item_minsell = table_row.find_all('div', class_='label-md')[1].text.strip()

    if item_type == 'Resource':
        with open(resources_file, 'a') as file:
            file.write(f'{item_id};{item_name};{item_minsell};{item_rarity};{item_type}\n')
        file.close()

    if item_faction != '':
        with open(craftables_file, 'a') as file:
            file.write(f'{item_id};{item_name};{item_minsell};{item_faction};{item_rarity};{item_type};{get_craft_materials(item_id)}\n')
        file.close()

'''
        if item_rarity == 'Common':
            obj = CommonCraftable(
                item_id, item_name, item_minsell, item_type, item_faction, item_rarity, get_craft_materials(item_id)
            )
            with open(dict_commons, 'a') as dict_file:
                dict_file.write(json.dumps(obj.__dict__))
                dict_file.write('\n')
            dict_file.close()

        if item_rarity == 'Rare':
            obj = RareCraftable(
                item_id, item_name, item_minsell, item_type, item_faction, item_rarity, get_craft_materials(item_id)
            )
            with open(dict_rares, 'a') as dict_file:
                dict_file.write(json.dumps(obj.__dict__))
                dict_file.write('\n')
            dict_file.close()

        if item_rarity == 'Epic':
            obj = EpicCraftable(
                item_id, item_name, item_minsell, item_type, item_faction, item_rarity, get_craft_materials(item_id)
            )
            with open(dict_epics, 'a') as dict_file:
                dict_file.write(json.dumps(obj.__dict__))
                dict_file.write('\n')
            dict_file.close()

        if item_rarity == 'Legendary':
            obj = LegendaryCraftable(
                item_id, item_name, item_minsell, item_type, item_faction, item_rarity, get_craft_materials(item_id)
            )
            with open(dict_legendaries, 'a') as dict_file:
                dict_file.write(json.dumps(obj.__dict__))
                dict_file.write('\n')
            dict_file.close()

        if item_rarity == 'Relic':
            obj = RelicCraftable(
                item_id, item_name, item_minsell, item_type, item_faction, item_rarity, get_craft_materials(item_id)
            )
            with open(dict_relics, 'a') as dict_file:
                dict_file.write(json.dumps(obj.__dict__))
                dict_file.write('\n')
            dict_file.close()
'''

# print(item_id, item_name, item_minsell, item_type, item_faction, item_rarity)
