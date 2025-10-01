from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id = id, condition = condition)
        self.fabric = fabric

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} It is made from {self.fabric} fabric."
