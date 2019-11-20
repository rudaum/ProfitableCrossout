class CrossoutItem:
    def __init__(self):
        self.x = 1


class Resource(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity


class CommonCraftable(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class RareCraftable(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class EpicCraftable(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class LegendaryCraftable(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]


class RelicCraftable(CrossoutItem):
    def __init__(self, uid, name, value, type, faction, rarity):
        self.uid = uid
        self.name = name
        self.value = value
        self.type = type
        self.faction = faction
        self.rarity = rarity
        self.prod_materials = [1]