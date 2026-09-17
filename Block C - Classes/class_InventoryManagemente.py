class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, quantity):
        if product_name not in self.products:
            self.products[product_name] = quantity
        else:
            self.products[product_name] += quantity
    def remove_product(self, product_name, quantity):
        if product_name in self.products:
            if self.products[product_name] >= quantity:
                self.products[product_name] -= quantity
            else:
                print(f"Not enough {product_name} in stock to remove {quantity}.")
        else:
            print(f"{product_name} does not exist in inventory.")
    def restock_needed(self):
        products_needed = []
        for product, quantity in self.products.items():
            if quantity < 5:
                products_needed.append((product, quantity))
        if not products_needed:
            print("No products need restocking.")
        return products_needed


inventory = Inventory()
inventory.add_product("shirts", 12)
inventory.add_product("pants", 3)
inventory.add_product("shoes", 4)
print(inventory.restock_needed())

inventory.remove_product("shirts", 5)
print(inventory.products)