import uuid

class Item:
    def __init__(self, id = None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}.")
    
    def condition_description(self):
        descriptions = {
            0: "Very old — oh no!!!!",
            1: "Seen better days",
            2: "Used but okay",
            3: "Good shape",
            4: "Almost new!",
            5: "Brand new!"
        }
        return descriptions[self.condition]
    
        