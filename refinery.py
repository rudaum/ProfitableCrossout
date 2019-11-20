from grabber import get_crossoutdb_Items

items = get_crossoutdb_Items()


def get_resources():
    resources = []
    for item in items:
        if item.type == 'Resource':
            resources.append(item)
    return resources


def get_craftables():
    craftables = []
    for item in items:
        if item.faction != '':
            craftables.append(item)
    return craftables
