import requests
from bs4 import BeautifulSoup
from classes import Resource, CommonCraftable, RareCraftable, EpicCraftable, LegendaryCraftable, RelicCraftable


def getCrossoutDBItems():
    url = 'https://crossoutdb.com/#length=-1.'
    print('oi')
    response = requests.get(url)
    print('oi')
    # parse html
    crossoutdb_page = BeautifulSoup(response.content, 'html.parser')

    resources = common_craftables = rare_craftables = epic_craftables = legendary_craftables = relic_craftables = []

    # Grabbing Items
    for table_row in crossoutdb_page.find_all('tr', class_='selected-row'):
        item_id = table_row.find('a')['href']
        item_name = table_row.find('h4', class_="item-title").text
        item_rarity = table_row.find('span').text
        item_faction = table_row.find_all('div', class_='label-md-left')[0].text
        item_type = table_row.find_all('div', class_='label-md-left')[2].text
        item_minsell = table_row.find_all('div', class_='label-md')[1].text

        if item_type == 'Resource':
            resources.append(Resource(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))
        if item_faction != '':
            if item_rarity == 'Common':
                common_craftables.append(CommonCraftable(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))
            if item_rarity == 'Rare':
                rare_craftables.append(RareCraftable(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))
            if item_rarity == 'Epic':
                epic_craftables.append(EpicCraftable(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))
            if item_rarity == 'Legendary':
                legendary_craftables.append(LegendaryCraftable(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))
            if item_rarity == 'Relic':
                relic_craftables.append(RelicCraftable(item_id, item_name, item_minsell, item_type, item_faction, item_rarity))

    item_list = [resources, common_craftables, rare_craftables, epic_craftables, legendary_craftables, relic_craftables]
    # print(item_id, item_name, item_minsell, item_type, item_faction, item_rarity)
    return item_list
