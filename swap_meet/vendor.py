from swap_meet.item import Item

class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None    
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            
            other_vendor.remove(their_item)
            self.add(their_item)
            
            return True
            
        return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_first_item = self.inventory[0]
        other_vendor_item = other_vendor.inventory[0]

        self.inventory.pop(0)
        other_vendor.inventory.pop(0)

        self.inventory.insert(0, other_vendor_item)
        other_vendor.inventory.insert(0, my_first_item)

        return True
    
    def get_by_category(self, category):
        matched_item_category = [
            item for item in self.inventory 
            if item.get_category() == category
            ]
        
        return matched_item_category
    
    def get_best_by_category(self, category):
        matched_item_category = self.get_by_category(category)
        
        if not matched_item_category:
            return None
        
        item_in_best_condition = None
        
        for item in matched_item_category:
            if (
                item_in_best_condition is None 
                or item.condition > item_in_best_condition.condition
                ):
                item_in_best_condition = item
        return item_in_best_condition
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        
        if not my_best or not their_best:
            return False
        
        self.remove(my_best)
        other_vendor.remove(their_best)
        
        self.inventory.insert(0, their_best)
        other_vendor.inventory.insert(0, my_best)
        
        return True
        
        
        
        

