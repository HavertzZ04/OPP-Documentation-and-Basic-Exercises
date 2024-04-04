"""
Create a food order entry system for a restaurant that allows customers to place orders and calculate the total bill.
"""

class ItemMenu:
    def __init__(self, item_name, price, stock):
        self.item_name = item_name.title()
        self.price = price
        self.stock = stock
        
        
class Menu:
    def __init__(self):
        self.menu_list = []
    
    def add(self, *item):
        self.menu_list.extend(item)
    
    def show_menu(self):
        menu_names = []
        for i in self.menu_list:
            menu_names.append(i.item_name)
        return menu_names
    
    def search(self, item):
        serching_item = False
        for i in self.menu_list:
            if item.title() == i.item_name:
                print(f"Product: {i.item_name} // Price: {i.price} // {i.stock}")
                serching_item = True
        if not serching_item:
            print("We have not that food on our menu")
    
class Order:
    def __init__(self):
        self.order_list = []
    
    def add(self, *item):
        self.order_list.extend(item)
    
    def calculate_total(self):
        total = 0
        for i in self.order_list:
            total += i.price
        return total
    
    def show_details(self):
        order_names = []
        for i in self.order_list:
            order_names.append(i.item_name)
        return order_names
    

class Customer:
    def __init__(self, cx_name):
        self.cx_name = cx_name
        self.cx_orders = []
    
    #Add items to orders
    def add_items(self, *order):
        self.cx_orders.extend(order)
    
    #Pay order
    def pay(self):
        bill = 0
        for i in self.cx_orders:
            bill += i.price
        return (f"Total bill for {self.cx_name}: {bill}") 
    
    
pasta = ItemMenu("pasta", 12500, 5)
rice = ItemMenu("rice", 7500, 2)
salad = ItemMenu("salad", 5200, 10)

menu1 = Menu()
menu1.add(pasta, rice, salad)

print(menu1.show_menu())
print()

menu1.search("perro")
print()

order1 = Order()
order1.add(rice, salad)
print(order1.show_details())
print()
print(order1.calculate_total())
print()

cx1 = Customer("Johan")
cx1.add_items(rice, salad)
print(cx1.pay())