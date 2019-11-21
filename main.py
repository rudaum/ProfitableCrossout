from classes import Resource, Craftable, CommonCraftable, RareCraftable, EpicCraftable, LegendaryCraftable, RelicCraftable
from settings import *

craftables = []
resources = []
commons = []
rares = []
epic = []
legendaries = []
relics = []


def retrieve_craftables():
    # Retrieving Resources
    with open(resources_file, 'r') as file:
        for line in file.readlines():
            resources.append(
                Resource(line.strip())
            )
    file.close()

    # Retrieving Common Craftables
    with open(craftables_file, 'r') as file:
        for line in file.readlines():
            resources.append(
                Craftable(line.strip())
            )
    file.close()



retrieve_craftables()
