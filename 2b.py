 #2(B) 
 
#Design Python classes for Product, Inventory, and Sales to        
#manage product information, track inventory levels, and 
#record sales transactions, respectively, using inheritance. 

class Product: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 
class Inventory(Product): 
    def __init__(self, name, price, quantity): 
        super().__init__(name, price) 
        self.quantity = quantity 
    def update_stock(self, amount): 
        self.quantity += amount 
    def check_stock(self): 
        return self.quantity 
class Sales(Inventory): 
    def __init__(self, name, price, quantity): 
        super().__init__(name, price, quantity) 
        self.sales_record = [] 
    def record_sale(self, quantity_sold): 
        if quantity_sold <= self.quantity: 

            self.quantity -= quantity_sold 
            total_price = self.price * quantity_sold 
            self.sales_record.append((self.name, quantity_sold, total_price)) 
            print(f"Sold {quantity_sold} units of {self.name}.") 
        else: 
            print("Insufficient stock for sale.") 
# User input 
product_name = input("Enter product name: ") 
product_price = float(input("Enter product price: ")) 
initial_quantity = int(input("Enter initial inventory quantity: ")) 
# Create inventory object 
product = Inventory(product_name, product_price, initial_quantity) 
# Record a sale 
sale_quantity = int(input("Enter quantity to sell: ")) 
sales = Sales(product_name, product_price, initial_quantity) 
sales.record_sale(sale_quantity) 
# Output 
print(f"Remaining stock of {product.name}: {product.check_stock()}") 
print("Sales record:", sales.sales_record)