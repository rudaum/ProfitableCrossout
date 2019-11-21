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
    with open(resources_file, 'r') as dict_file:
        for line in dict_file.readlines():
            print(line.split())
            resources.append(
                Resource(line.split(';'))
            )



retrieve_craftables()
