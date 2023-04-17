class ItemToPurchase:
    def __init__ (self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "non"
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${int(self.item_quantity) * int(self.item_price)}")
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name = "non", current_date = "January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, newItem):
        for item in self.cart_items:
            if item.item_name == newItem.item_name:
                newItem.item_description = item.item_description
                newItem.item_price = item.item_price
                self.cart_items.remove(item)
                self.cart_items.append(newItem)
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += int(item.item_quantity)
        return total
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += int(item.item_price) * int(item.item_quantity)
        return total
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print("\nTotal: $" + str(self.get_cost_of_cart()) + "\n")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)
        print()
    def print_menu(self):
        print("MENU")
        print("a - Add item to cart\nr - Remove item from cart\nc - Change item quantity")
        print("i - Output items' descriptions\no - Output shopping cart\nq - Quit")
    def execute_menu(self, choice):
        if choice == "o":
            print("\nOUTPUT SHOPPING CART")
            self.print_total()
        if choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()
        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = input("Enter the item price:\n")
            quant = input("Enter the item quantity:\n\n")
            newItem = ItemToPurchase()
            newItem.item_name = name
            newItem.item_description = desc
            newItem.item_price = price
            newItem.item_quantity = quant
            self.add_item(newItem)
        if choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            self.remove_item(name)
            print()
        if choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quant = input("Enter the new quantity:\n")
            newItem = ItemToPurchase()
            newItem.item_name = name
            newItem.item_quantity = quant
            self.modify_item(newItem)
            print()

valid_list = ["o", "i", "a", "r", "c"]
customer_name = input("Enter customer's name:\n")
date = input("Enter today's date:\n")

print(f"\nCustomer name: {customer_name}\nToday's date: {date}\n")

cart = ShoppingCart()
cart.customer_name = customer_name
cart.current_date = date

choice = ""
cart.print_menu()

while choice != "q":
    choice = input("\nChoose an option:")
    if choice in valid_list:
        cart.execute_menu(choice)
        cart.print_menu()
print()