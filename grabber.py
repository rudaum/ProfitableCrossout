import os
import requests
import time
from bs4 import BeautifulSoup

from settings import *


def get_craft_materials(uid):
    url_ = 'https://crossoutdb.com/{}'.format(uid)
    craft_materials = {}
    response_ = requests.get(url_)
    # parse html
    item_page = BeautifulSoup(response_.content, 'html.parser')
    for row in item_page.findAll('tr', class_="depth-1"):
        if row.attrs['data-parentuniqueid'] == '0':
            material = row.find('a', style="font-weight: bold;").text.strip()
            amount = row.find('div', class_="label-md pull-left").text.strip().split()[0]
            # unit_value = row.find('div', class_="recipe-price label-md rec-right").text.strip().split()[0]
            craft_materials[material] = amount
    return craft_materials


while True:
    # Setting and emptying the Data Files
    open(cratmp_file, 'w').close()
    open(restmp_file, 'w').close()

    # CrossoutDB Main Page
    url = 'https://crossoutdb.com/#length=-1.'
    response = requests.get(url)

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
        item_maxbuy = table_row.find_all('div', class_='label-md')[3].text.strip()

        if item_type == 'Resource':
            with open(restmp_file, 'a') as file:
                file.write(f'{item_id};{item_name};{item_minsell};{item_maxbuy};{item_rarity};{item_type}\n')
            file.close()

        if item_faction != '':
            with open(cratmp_file, 'a') as file:
                file.write(f'{item_id};{item_name};{item_minsell};{item_maxbuy};{item_faction};{item_rarity};{item_type};'
                           f'{get_craft_materials(item_id)}\n')
            file.close()

    # Manually Adding Workbenches and Others as Resources
    with open(restmp_file, 'a') as file:
        file.write(f'item/392;\'Calendar\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/393;\'Graffiti Dusk\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/443;\'Duck\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/444;\'Stop!\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/446;Rare Minimum Bench Cost;4.5;0;Common;Resource\n')
        file.write(f'item/447;Epic Minimum Bench Cost;18;0;Common;Resource\n')
        file.write(f'item/448;Legendary Minimum Bench Cost;72;0;Common;Resource\n')
        file.write(f'item/449;Relic Minimum Bench Cost;0;0;Common;Resource\n')
        file.write(f'item/459;\'Alligator\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/461;\'Blackboard\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/466;Skins Minimum Bench Cost;150;0;Common;Resource\n')
        file.write(f'item/469;\'Small speaker\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/470;\'No escape\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/517;\'Test Dummy\' fragment;0;0;Rare;Resource\n')
        file.write(f'item/522;Hazardous sweets x100;0.4;0;Common;Resource\n')
    file.close()

    os.replace(restmp_file, resources_file)
    os.replace(cratmp_file, craftables_file)
    time.sleep(60)
