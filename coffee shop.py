
coffee_prices = {
    "Espresso": 2.50,
    "Americano": 3.00,
    "Latte": 2.50,
    "Cappuccino": 3.00,
    "Macchiato": 2.50,
    "Mocha": 3.50,
    "Flat White": 2.50
}

size_prices = {
    "M": 0.00,  # Default size, no extra cost
    "L": 1.00,  # Large size costs +1 pound
    "XL": 1.50  # Extra-large costs +1.5 pounds
}


print("Available coffee types: ", ", ".join(coffee_prices.keys()))
coffee_type = input("Enter the coffee type: ").strip().title()


if coffee_type not in coffee_prices:
    print("Invalid coffee type! Please enter a valid option.")
    exit()


size = input("Enter cup size (M/L/XL): ").strip().upper()


if size not in size_prices:
    print("Invalid size! Please enter M, L, or XL.")
    exit()


eat_in = input("Eat in or Takeaway (E/T): ").strip().upper()


if eat_in not in ["E", "T"]:
    print("Invalid choice! Please enter E for Eat-in or T for Takeaway.")
    exit()

total_cost = coffee_prices[coffee_type] + size_prices[size] + (1.00 if eat_in == "T" else 0.00)

# showing total price

print(f"\nOrder Summary:")
print(f"- Coffee: {coffee_type}")
print(f"- Size: {size}")
print(f"- Takeaway: {'Yes' if eat_in == 'T' else 'No'}")
print(f"- Total Price: £{total_cost:.2f}")
