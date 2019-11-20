from grabber import get_crossoutdb_items

items = get_crossoutdb_items()
resources = items[0]
commons = items[1]
rares = items[2]
epic = items[3]
legendaries = items[4]
relics = items[5]


print(resources[0].name)
print(relics[1].name)
print(commons[0].name)