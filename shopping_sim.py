import datetime
 
# Product catalog
products = {
    "Bread": 2.0,
    "Milk": 1.5,
    "Eggs": 3.0,
    "Rice": 4.5,
    "Apple": 0.8
}

# Store user cart
cart = {}

print("🛒 Welcome to the Market Simulator!")
print("Here are the available products:")

# Show products
for item, price in products.items():
    print(f"- {item}: ${price}")

while True:
    choice = input("\nEnter product name to buy (or 'done' to checkout): ").title()

    if choice == "Done":
        break

    if choice not in products:
        print("❌ Product not available.")
        continue

    try:
        quantity = int(input(f"How many {choice}s do you want to buy? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Add to cart
    if choice in cart:
        cart[choice] += quantity
    else:
        cart[choice] = quantity

print("\n🧾 Your Receipt")
total = 0
for item, qty in cart.items():
    cost = products[item] * qty
    total += cost
    print(f"{qty}x {item} → ${cost:.2f}")

print("--------------------------")
print(f"Total: ${total:.2f}")
print(f"Cashier: Emily")
print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🙏 Thank you for shopping with us! Come back soon!")
