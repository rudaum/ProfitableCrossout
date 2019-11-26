class Resource:
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
        self.uid, self.name, self.value, self.faction, self.rarity, self.type, craft_materials \
            = csv_value.split(';')
        self.craft_materials = eval(craft_materials)
        self.prod_cost = 0
        self.resources_list = []
        self.craftables_list = []
        self.buy_or_craft = ''


class market_advisor:
    def __init__(self, craftable):
        self.craftable = craftable
        self.buy_list = []
        self.craft_list = []


