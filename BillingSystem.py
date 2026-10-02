class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = float(price)
        self.quantity = int(quantity)

    def item_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_amount(self):
        return sum(product.item_total() for product in self.products)

    def display_bill(self):
        print("\n====================================")
        print("             BILL RECEIPT")
        print("====================================")

        if not self.products:
            print("No products added.")
            return

        for index, product in enumerate(self.products, start=1):
            print(f"{index}. {product.product_name:<15}{product.quantity:>2} x ${product.price:>7.2f} = ${product.item_total():>8.2f}")

        total = self.total_amount()
        print("------------------------------------")
        print(f"Total Amount: ${total:.2f}")
        print("====================================")


def main():
    bill = Bill()

    while True:
        choice = input("Do you want to add a product? (y/n): ").strip().lower()
        if choice != 'y':
            break

        try:
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity must be positive numbers.")
                continue

            bill.add_product(Product(product_name, price, quantity))
            print("Product added successfully.")

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    bill.display_bill()


if __name__ == "__main__":
    main()
