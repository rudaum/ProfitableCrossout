from classes import Resource, CommonCraftable, RareCraftable, EpicCraftable, LegendaryCraftable, RelicCraftable
from settings import *

resources = []
commons = []
rares = []
epic = []
legendaries = []
relics = []


def retrieve_craftables():
    # Retrieving Common Craftables
    with open(dict_commons, 'r') as dict_file:
        for line in dict_file.readlines():
            resources.append(
                Resource()
            )
            print(line)


retrieve_craftables()
