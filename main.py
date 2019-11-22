from classes import Resource, Craftable
from settings import *

resources = {}
craftables = {}


def retrieve_items():
    # Retrieving Resources
    with open(resources_file, 'r') as file:
        for line in file.readlines():
            resources[line.split(';')[1]] = Resource(line.strip())
    file.close()

    # Retrieving Craftables
    with open(craftables_file, 'r') as file:
        for line in file.readlines():
            craftables[line.split(';')[1]] = Craftable(line.strip())
    file.close()


def calc_prodcost(craftable):
    prod_cost = 0
    materials = eval(craftable.craft_materials)

    for material, quantity in materials.items():
        if 'Minimum Bench Cost' in material:
            partial_cost = workbench_cost[material] * int(quantity)
            prod_cost = prod_cost + partial_cost
            print(f'{material} costs: {partial_cost}')
        elif material in resources.keys():
            partial_cost = resources[material].unit_price * int(quantity)
            prod_cost = prod_cost + partial_cost
            print(f'{material} costs: {partial_cost}')
        elif material not in resources.keys():
            partial_cost = float(craftables[material].value) * int(quantity)
            prod_cost = prod_cost + partial_cost
            print(f'{material} costs: {partial_cost}')
    return prod_cost


retrieve_items()

craft = 'Harvester'
craftables[craft].prod_cost = calc_prodcost(craftables[craft])
print(f'Total Cost for {craft}: {craftables[craft].prod_cost}')
print(f'Min Sell Price for {craft}: {craftables[craft].value}')
print(f'Profit for {craft}: {float(craftables[craft].value) * 0.9 - craftables[craft].prod_cost}')
