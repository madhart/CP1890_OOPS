from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discountPercent: int

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 4.99, 50)
product3= Product("Economy Duct Tape, 60 yds, silver", 9.99, 20)
products = []
products.append(product1)
products.append(product2)
products.append(product3)
def introduction_menu():
    print("The Product Viewer program\n")
    print("PRODUCTS")
    for i, item in enumerate(products, start=1):
        print(f"{i}. {item.name}")

def main():
    while True:
        introduction_menu()
        print("\n")
        number_choice = input("Enter product number: ")
        print("\n")
        print(f"Name: {product1.name}")
        print(f"Price: {product1.price:.2f}")
        print(f"Discount Percent: \t\t {product1.discountPercent:d}%")
        print(f"Discount Amount: \t\t {product1.getDiscountAmount():.2f}")
        print(f"Discount Price: \t\t {product1.getDiscountPrice():.2f}")
        selection= input("\n View another product? (y/n): ")
        if selection == 'y':
            continue
        elif selection == 'n':
            break
        else:
            print("Invalid selection. Please try again.")
            continue

if __name__ == "__main__":
    main()