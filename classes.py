class Resource():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity

class CommonCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, resource, resource_amount):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.resource = resource
        self.resource_amount = resource_amount


class RareCraftable():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class EpicCraftable():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class LegendaryCraftable():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class RelicCraftable():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]