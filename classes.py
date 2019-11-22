class Resource():
    def __init__(self, csv_value):
        self.uid, self.name, self.value, self.rarity, self.type = csv_value.split(';')
        self.unit_price = self.unit_price()

    def unit_price(self):
        if 'x1000' in self.name:
            return float(self.value) / 1000
        elif 'x100' in self.name:
            return float(self.value) / 100
        elif 'x10' in self.name:
            return float(self.value) / 10
        else:
            return float(self.value)


class Craftable:
    def __init__(self, csv_value):
        self.uid, self.name, self.value, self.faction, self.rarity, self.type, self.craft_materials \
            = csv_value.split(';')
        self.prod_cost = 0
        self.buy_dict = {}
        self.craft_dict = {}


class CommonCraftable:
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class RareCraftable:
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class EpicCraftable:
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class LegendaryCraftable:
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class RelicCraftable:
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials
