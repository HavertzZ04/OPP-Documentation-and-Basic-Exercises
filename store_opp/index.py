'''
    Create an online shopping system that allows users to browse products, add items to their cart, remove items from their cart, and place orders.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def product_details(self):
        return f"Product: {self.name} / Price: ${self.price} / Quantity: {self.quantity}"
    

class ShoppingCart:
    def __init__(self):
        self.cart_products_list = []
    
    def add_to_cart(self, product):
        for item in self.cart_products_list:
            if item.name == product.name:
                item.quantity += 1
                return True
        
        self.cart_products_list.append(product)
        return True
    
    def remove_from_cart(self, product_name):
        for item in self.cart_products_list:
            if item.name == product_name:
                if item.quantity > 1:
                    item.quantity -= 1
                else:
                    self.cart_products_list.remove(item)
                return True
            
        print(f"The product '{product_name}' is not in your cart.")
        return False
    
    def calculate_cart_items(self):
        total_items = sum(item.quantity for item in self.cart_products_list)
        return total_items
    
    def display_cart_items(self):
        for item in self.cart_products_list:
            print(item.product_details())
    
    
class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total_price = self.calculate_total_price()
    
    def calculate_total_price(self):
        total_price = sum(item.price * item.quantity for item in self.cart.cart_products_list)
        return total_price
    
    def order_details(self):
        print(f"Order for user {self.user.name}:")
        self.cart.display_cart_items()
        print(f"Total Price: ${self.total_price}")


class User:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def add_to_cart(self, product, cart):
        cart.add_to_cart(product)
        print(f"{product.name} added to the cart.")
    
    def remove_from_cart(self, product_name, cart):
        if cart.remove_from_cart(product_name):
            print(f"{product_name} removed from the cart.")
    
    def place_order(self, cart):
        if cart.cart_products_list:
            order = Order(self, cart)
            self.orders.append(order)
            print("Order placed successfully.")
            cart.cart_products_list = []
        else:
            print("Your cart is empty. Please add some products before placing an order.")
    
    def view_orders_history(self):
        if self.orders:
            print("Orders History:")
            for order in self.orders:
                order.order_details()
        else:
            print("No orders placed yet.")


# Ejemplo de uso
rice = Product("Rice", 12.10, 2)
apple = Product("Apple", 0.99, 5)
banana = Product("Banana", 0.50, 10)

user = User("Alice")
cart = ShoppingCart()

user.add_to_cart(rice, cart)
user.add_to_cart(apple, cart)
user.add_to_cart(banana, cart)

user.remove_from_cart("Rice", cart)
user.remove_from_cart("Orange", cart)

user.place_order(cart)
user.view_orders_history()