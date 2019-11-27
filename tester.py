from settings import craftables_file, resources_file
from classes import Craftable, Resource

craftables = {}
resources = {}
advisors = {}


def set_prodmaterials(_craftable):
    """
    Recursively checks which materials are needed in total to craft an Item.
    """
    partial_resources = []
    partial_craftables = []
    _craftable.resources_list = []
    _craftable.craftables_list = []

    # Checking for Production Materials
    for material, quantity in _craftable.craft_materials.items():
        # Checking for Resources or Workbench Need
        if 'Minimum Bench Cost' in material or material in resources.keys():
            _craftable.resources_list.append([material, int(quantity)])
            _craftable.res_totalcost = float(_craftable.res_totalcost + resources[material].unit_price * int(quantity))

        # Check for sub-craftables as a need
        elif material not in resources.keys():
            _craftable.craftables_list.append([material, int(quantity)])

    return partial_resources, partial_craftables


def get_prodcost(_craftable, tab):
    """
    Calculates the production cost for a given Item Object. If there are other craftable Items as needed as material,
    then this method is RECURSIVELY called.
    """
    #print(f'{tab}{_craftable.name} ({_craftable.value}):')
    if _craftable.prod_cost == 0:
        prodcost = 0

        tab = tab + '  '

        # If there are Craftable Items as required materials ....
        if len(_craftable.craftables_list) > 0:
            for craft, amount in _craftable.craftables_list:
                # partial_cost = round(float(craftables[craft].value) * amount, 2)
                for loop in range(amount):
                    partial_cost = get_prodcost(craftables[craft], tab)
                    # If the prod cost of the item is more expensive than the buy cost
                    if partial_cost >= float(craftables[craft].value):
                        partial_cost = float(craftables[craft].value)
                        craftables[craft].buy_or_craft = 'buy'
                        # print(f'{tab}Buy item {craft}')
                    else:
                        craftables[craft].buy_or_craft = 'craft'
                        # print(f'{tab}Craft item {craft}')
                    prodcost = prodcost + partial_cost

        # If the Total PROD Cost (prod_cost + res_totalcost) is cheaper the the market value:
        prodcost = prodcost + _craftable.res_totalcost
        if prodcost < float(_craftable.value):
            for resource, amount in _craftable.resources_list:
                partial_cost = round(float(resources[resource].unit_price) * amount, 2)
                # print(f'{tab}{resource} Cost: {partial_cost}')

        # print(f'{tab}Total Prod Cost: {round(prodcost, 2)}')
        if prodcost < float(_craftable.value):
            # print(f'{tab}Craft item {_craftable.name}')
            _craftable.buy_or_craft = 'craft'
        else:
            # print(f'{tab}Buy item {_craftable.name}')
            _craftable.buy_or_craft = 'buy'
        return prodcost
    else:
        return _craftable.prod_cost

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

# Setting the Craftable Materials of each item
for craftable in craftables.values():
    set_prodmaterials(craftable)

# Setting the Prod Cost of each Craftable
for craftable in craftables.values():
    craftable.prod_cost = get_prodcost(craftable, '  ')
    craftable.profit = round(craftable.value_after_taxes - craftable.prod_cost, 2)

# Getting List of Profitable Items:
sort_items = []
def sortSecond(val):
    return val[1]


for craftable in craftables.values():
    if craftable.profit > 0:
        sort_items.append([craftable.name, round(craftable.profit / craftable.craft_time, 2)])
sort_items.sort(key=sortSecond)

for sorted in sort_items:
    craftable = craftables[sorted[0]]
    item = craftable.name
    profit_per_min = round(craftable.profit / craftable.craft_time, 2)
    print(f'{item} (Craft Time: {craftable.craft_time} minutes) Profit is: {craftable.profit} - Profit / Min = {profit_per_min}')





