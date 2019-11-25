from settings import craftables_file, resources_file
from classes import Craftable, Resource

craftables = {}
resources = {}


def set_prodmaterials(_craftable):
    """
    Recursively checks which materials are needed in total to craft an Item.
    """
    partial_resources = []
    partial_craftables = []

    # Checking for Production Materials
    for material, quantity in _craftable.craft_materials.items():
        # Checking for Resources or Workbench Need
        if 'Minimum Bench Cost' in material or material in resources.keys():
            _craftable.resources_list.append([material, int(quantity)])

        # Check for sub-craftables as a need
        elif material not in resources.keys():
            _craftable.craftables_list.append([material, int(quantity)])
    return partial_resources, partial_craftables


def get_prodcost(_craftable, tab):
    """
    Calculates the production cost for a given Item Object. If there are other craftable Items as needed as material,
    then this method is RECURSIVELY called.
    """
    prodcost = 0

    print(f'{tab}{_craftable.name}:')
    tab = tab + '  '
    for resource, amount in _craftable.resources_list:
        partial_cost = round(float(resources[resource].unit_price) * amount, 2)
        prodcost = prodcost + partial_cost
        print(f'{tab}{resource} Cost: {partial_cost}')

    # If there are Craftable Items as required materials ....
    if len(_craftable.craftables_list) > 0:
        for craft, amount in _craftable.craftables_list:
            # partial_cost = round(float(craftables[craft].value) * amount, 2)
            for loop in range(amount):
                get_prodcost(craftables[craft], tab)
                # If the prod cost of the item is cheaper than the buy cost, calculate the crafting value
                # if partial_cost < craftables[craft].value:

    return prodcost

# Reading the Resources CSV file and feeding a Dictionary of Resources Objects
with open(resources_file, 'r') as file:
    for line in file.readlines():
        resources[line.split(';')[1]] = Resource(line.strip())
file.close()

# Reading the Craftables CSV file and feeding a Dictionary of craftables Objects
with open(craftables_file, 'r') as file:
    for line in file.readlines():
        craftables[line.split(';')[1]] = Craftable(line.strip())
file.close()

for craftable in craftables.keys():
    set_prodmaterials(craftables[craftable])


item = 'Gasgen'
get_prodcost(craftables[item], '')

"""
print(f'Shop List for {item}: {craftables[item].craft_materials}')
print(f'Total Production Cost: {craftables[item].prod_cost}')
print(f'Market Value: {craftables[item].value}')
print(f'Buy or Craft Item? {craftables[item].buy_or_craft}')
"""