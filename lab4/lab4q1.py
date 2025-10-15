# lab4q1.py
# Customer class
class Customer:
    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address
# Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
# Equality, Representation, and String Methods
    def __eq__(self, other):
        return isinstance(other, Customer) and self._name == other._name and self._address == other._address

    def __repr__(self):
        return f"Customer(name='{self._name}', address='{self._address}')"

    def __str__(self):
        return f"{self._name}, {self._address}"

class Product:
    def __init__(self, productid: int, product_name: str, price: float):
        self._productid = productid
        self._product_name = product_name
        self._price = price

    @property
    def productid(self):
        return self._productid

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        
    def __eq__(self, other):
        return isinstance(other, Product) and self._productid == other._productid

    def __repr__(self):
        return f"Product(id={self._productid}, name='{self._product_name}', price={self._price})"

    def __str__(self):
        return f"{self._product_name} (${self._price})"


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self._product = product
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def get_total_price(self):
        return self._product.price * self._quantity

    def __eq__(self, other):
        return isinstance(other, OrderItem) and self._product == other._product

    def __repr__(self):
        return f"OrderItem(product={repr(self._product)}, quantity={self._quantity})"

    def __str__(self):
        return f"{self._quantity} × {self._product}"


class Order:
    def __init__(self, orderid: int, customer: Customer):
        self._orderid = orderid
        self._customer = customer
        self._order_items = []

    @property
    def orderid(self):
        return self._orderid

    @property
    def customer(self):
        return self._customer

    @property
    def order_items(self):
        return self._order_items

    def add_item(self, product: Product, quantity: int):
        for item in self._order_items:
            if item.product == product:
                item.quantity += quantity
                return
        self._order_items.append(OrderItem(product, quantity))

    def remove_item(self, productid: int):
        self._order_items = [item for item in self._order_items if item.product.productid != productid]

    def find_largest_item(self):
        if not self._order_items:
            return None
        return max(self._order_items, key=lambda item: item.quantity)

    def get_discount_value(self, discount_rate: float):
        return self.get_total() * discount_rate

    def get_total(self):
        return sum(item.get_total_price() for item in self._order_items)

    def __eq__(self, other):
        return isinstance(other, Order) and self._orderid == other._orderid

    def __repr__(self):
        return f"Order(id={self._orderid}, customer={repr(self._customer)}, items={repr(self._order_items)})"
# String representation of the invoice
    def __str__(self):
        header = f"{'='*40}\n       INVOICE - Order #{self._orderid}\n{'='*40}\n"
        customer_info = f"Customer: {self._customer.name}\nAddress: {self._customer.address}\n{'-'*40}\n"
        items_header = f"{'Product':15}{'Qty':>5}{'Price':>10}{'Total':>10}\n{'-'*40}\n"
        items_str = ""
        for item in self._order_items:
            items_str += f"{item.product.product_name:15}{item.quantity:>5}{item.product.price:>10.2f}{item.get_total_price():>10.2f}\n"
        footer = f"{'-'*40}\nGrand Total:{self.get_total():>28.2f}\n{'='*40}"
        return header + customer_info + items_header + items_str + footer


if __name__ == "__main__":
    # Creating
    # customer
    customer1 = Customer("Anish Khadka", "123 SF Street, CA")

    # Create grocery products
    product1 = Product(101, "Apples", 2.50)
    product2 = Product(102, "Bread", 3.00)
    product3 = Product(103, "Milk", 4.20)

    # Create order
    order = Order(202, customer1)

    # Add grocery items
    order.add_item(product1, 4)  # 4 Apples
    order.add_item(product2, 2)  # 2 Bread
    order.add_item(product3, 1)  # 1 Milk

    print(order)

    # Remove an item
    order.remove_item(102)  # remove Bread
    print("\nAfter removing Bread:")
    print(order)

    # Find largest item
    print("\nLargest item in order:", order.find_largest_item())

    # Apply discount
    print("\nDiscount (10%): $", order.get_discount_value(0.1))