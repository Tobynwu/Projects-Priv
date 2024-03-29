# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""
class ItemToPurchase:
    
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
    
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, name='none', date='January 1, 2016', items=None):
        self.customer_name = name
        self.current_date = date
        self.cart_items = items if items is not None else []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self, item):
        found = False
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                found = True
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                if item.item_description != 'none':
                    cart_item.item_description = item.item_description
                break
        if not found:
            print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            print("\nTotal: $0")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()
def print_menu(cart):
    # Display the menu options and perform the selected operation based on user input

    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')
    print(menu)

    # Loop until the user quits
    while True:
        command = input('Choose an option:\n').strip().lower()

        # Validate command and continue until user enters a valid command
        if command not in ['a', 'o', 'i', 'q', 'r', 'c']:
            continue

        if command == 'a':
            # Add an item to the cart
            print("\nADD ITEM TO CART")
            item_name = input('Enter the item name:\n').strip()
            item_description = input('Enter the item description:\n').strip()
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

        elif command == 'o':
            # Output shopping cart
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif command == 'i':
            # Output item descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == 'r':
            # Remove an item from the cart
            print("REMOVE ITEM FROM CART")
            item_name = input('Enter name of item to remove:\n').strip()
            cart.remove_item(item_name)

        elif command == 'c':
            # Change item quantity
            print("\nCHANGE ITEM QUANTITY")
            item_name = input('Enter the item name:\n').strip()
            qty = int(input('Enter the new quantity:\n'))
            item = ItemToPurchase(item_name, 0, qty)
            cart.modify_item(item)

        elif command == 'q':        
            break
        print(menu)

if __name__ == "__main__":
    # Input customer name and today's date
    customer_name = input("Enter customer's name:\n").strip()
    current_date = input("Enter today's date:\n").strip()

    # Display customer name and today's date
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create a shopping cart object
    cart = ShoppingCart(customer_name, current_date)

    # Display the menu and handle user input
    print_menu(cart)