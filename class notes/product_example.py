from objects_introduction import Product

# Creating the products
product1 = Product("Stanley Hammer",9.99, 5)
product2 = Product("Quartet Marker", 2.00, 4)

print("Product Data")
print(f"Product Name: {product1.name}")
print(f"Product Price: {product1.price:.2f}")
print(f"Discount Percen: \t\t {product1.discountPercent:d}%")

print(f"Discount Amount: \t\t {product1.getDiscountAmount():.2f}")
print(f"Discount Price: \t\t {product1.getDiscountPrice():.2f}