


resources = items[0]
commons = items[1]
rares = items[2]
epic = items[3]
legendaries = items[4]
relics = items[5]


def get_resource_by_name(name):
    for item in resources:
        if item.name == name:
            return item
