class Resource():
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity


class Craftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class CommonCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class RareCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class EpicCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class LegendaryCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials


class RelicCraftable():
    def __init__(self, uid, name, value, type, faction, rarity, craft_materials):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.craft_materials = craft_materials
