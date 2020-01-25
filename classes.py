class Resource:
    def __init__(self, csv_value):
        self.uid, self.name, self.value, self.max_buy, self.rarity, self.type = csv_value.split(';')
        self.unit_price = self.unit_price()
        self.sell_buy_delta_net = round(float(self.value) * 0.9 - float(self.max_buy), 2)

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
        self.uid, self.name, self.value, self.max_buy, self.faction, self.rarity, self.type, craft_materials, \
            = csv_value.split(';')
        self.craft_materials = eval(craft_materials)
        self.resources_list = []
        self.craftables_list = []
        self.prod_cost = 0
        self.res_totalcost = 0
        self.buy_or_craft = ''
        self.value_after_taxes = float(self.value) * 0.9
        self.sell_buy_delta_net = round(self.value_after_taxes - float(self.max_buy), 2)
        self.profit = 0
        self.craft_time = 0.084
        if self.rarity == 'Rare':
            self.craft_time = 15
        if self.rarity == 'Epic':
            self.craft_time = 360
        if self.rarity == 'Legendary':
            self.craft_time = 1260
        if self.rarity == 'Legendary':
            self.craft_time = 7200



