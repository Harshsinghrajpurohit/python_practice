
'''-----------------------------------------------------"Retail Billing Management System"--------------------------------------------------------'''
'''import time
class Customer:
    def login(self):
        self.name = input("Enter Your Name: ")
        while True:
            phone = int(input("Enter Phone Number: "))
            if len(str(phone)) == 10:
                self.phone = phone
                print("-----------------------------------")
                print(f"Welcome, {self.name}! Happy Shopping! ")
                time.sleep(2)
                print("-----------------------------------")
                break
            else:
                print("Invalid Phone Number! Must be 10 digits. Try again!")


class Product:
    products = {
        "Apple"  : 50,
        "Milk"   : 40,
        "Bread"  : 35,
        "Eggs"   : 80,
        "Butter" : 120
    }

    def display_products(self):
        print("===== Available Products =====")
        time.sleep(2)
        for i in Product.products:
            print(i, "-", "Rs.", Product.products[i])
        print("==============================")


class Cart:
    cart = {}

    def add_item(self):
        name = input("Enter the product name: ")
        quantity = int(input("Enter Quantity: "))
        if name in Product.products:
            if name in self.cart:
                self.cart[name] += quantity
            else:
                self.cart[name] = quantity
            print(f"{name} added to cart successfully!")
            time.sleep(3)
        else:
            print("Item not found!")

    def remove_item(self):
        name = input("Enter the product name: ")
        if name in self.cart:
            del self.cart[name]
            print(f"{name} removed from cart successfully!")
            time.sleep(3)
        else:
            print("Item not in cart!")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty!")
        else:
            print("======= Your Cart =======")
            time.sleep(1)
            for name in self.cart:
                quantity = self.cart[name]
                price = Product.products[name] * quantity
                print(name, "x", quantity, "-> Rs.", price)
            print("=========================")

    def generate_bill(self,cust):
        subtotal = 0
        if len(self.cart) == 0:
            print("Cart is empty!")
        else:
            print("========= BILL =========")
            time.sleep(3)
            print(f"Customer:{cust.name}")
            print(f"Phone Number:{cust.phone}")
            for name in self.cart:
                quantity = self.cart[name]
                price = Product.products[name] * quantity
                subtotal += price
                print(name, "x", quantity, "-> Rs.", price)

            gst = subtotal * 18 / 100
            if subtotal > 500:
                discount = subtotal * 10 / 100
            else:
                discount = 0
            total = subtotal + gst - discount

            print("------------------------")
            print("Subtotal   : Rs.", subtotal)
            print("GST (18%)  : Rs.", gst)
            print("Discount   : Rs.", discount)
            print("------------------------")
            print("Total Bill : Rs.", total)
            print("========================")

cust=Customer()
cust.login()
p = Product()
c = Cart()

print("Welcome to New Horizon Super Market!")

while True:
    print("\n======= MENU =======")
    print("1. View Products")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. Exit")
    print("====================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        p.display_products()
    elif choice == 2:
        c.add_item()
    elif choice == 3:
        c.remove_item()
    elif choice == 4:
        c.view_cart()
    elif choice == 5:
        c.generate_bill(cust)
    elif choice == 6:
        print("Thank You for Shopping! Goodbye!")
        time.sleep(3)
        break
    else:
        print("Invalid choice! Try again.")'''
