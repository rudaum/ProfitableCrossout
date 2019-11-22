from settings import craftables_file, resources_file, workbench_cost
from classes import Craftable, Resource

craftables = {}
resources = {}


def calc_prodcost(craftable):
    """
    Calculates the production cost for a given Item Object. If there are other craftable Items as needed as material,
    then this method is RECURSIVELY called.
    """
    prod_cost = 0
    materials = eval(craftable.craft_materials)

    for material, quantity in materials.items():
        if 'Minimum Bench Cost' in material:
            partial_cost = workbench_cost[material] * int(quantity)
            prod_cost = prod_cost + partial_cost
            #print(f'{material} costs: {partial_cost}')
            if material not in craftable.buy_dict:
                craftable.buy_dict[material] = int(quantity)
            else:
                craftable.buy_dict[material] = craftable.buy_dict[material] + int(quantity)
        elif material in resources.keys():
            partial_cost = resources[material].unit_price * int(quantity)
            prod_cost = prod_cost + partial_cost
            #print(f'{material} costs: {partial_cost}')
            if material not in craftable.buy_dict:
                craftable.buy_dict[material] = int(quantity)
            else:
                craftable.buy_dict[material] = craftable.buy_dict[material] + int(quantity)
        elif material not in resources.keys():

            craftables[material].prod_cost, buy, craft = calc_prodcost(craftables[material])

            print(f'{material} value is: {craftables[material].value}')
            print(f'{material} Prod Cost is: {craftables[material].prod_cost}')


            if float(craftables[material].prod_cost) < float(craftables[material].value):
                prod_cost = prod_cost + craftables[material].prod_cost
                if material not in craftable.buy_dict:
                    craftable.craft_dict[material] = int(quantity)
                else:
                    craftable.craft_dict[material] = craftable.craft_dict[material] + int(quantity)
            else:
                prod_cost = prod_cost + float(craftables[material].value)
                if material not in craftable.buy_dict:
                    craftable.buy_dict[material] = int(quantity)
                else:
                    craftable.buy_dict[material] = craftable.buy_dict[material] + int(quantity)

                #print(f'{material} costs: {partial_cost}')
    return [prod_cost, craftable.buy_dict, craftable.craft_dict]

with open(resources_file, 'r') as file:
    for line in file.readlines():
        resources[line.split(';')[1]] = Resource(line.strip())
file.close()

with open(craftables_file, 'r') as file:
    for line in file.readlines():
        craftables[line.split(';')[1]] = Craftable(line.strip())
file.close()

craft = 'Borer'
craftables[craft].prod_cost = calc_prodcost(craftables[craft])
print(f'Total Cost for {craft}: {craftables[craft].prod_cost}')
print(f'Min Sell Price for {craft}: {craftables[craft].value}')
print(f'Profit for {craft}: {float(craftables[craft].value) * 0.9 - craftables[craft].prod_cost[0]}')
print(craftables[craft].buy_dict)
print(craftables[craft].craft_dict)