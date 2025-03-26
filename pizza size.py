import math

def calculate_pizza_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

num_large_pizzas = int(input("Enter the number of large pizzas: "))
large_pizza_size = float(input("Enter the diameter of the large pizza (in inches): "))

num_small_pizzas = int(input("Enter the number of small pizzas: "))
small_pizza_diameter = float(input("Enter the diameter of the small pizza (in inches): "))


total_large_pizza_area = num_large_pizzas * calculate_pizza_area(large_pizza_size)
total_small_pizza_area = num_small_pizzas * calculate_pizza_area(small_pizza_diameter)

print(f"\nTotal area of {num_large_pizzas} large pizza(s): {total_large_pizza_area:.2f} square inches")
print(f"Total area of {num_small_pizzas} small pizza(s): {total_small_pizza_area:.2f} square inches")

if total_large_pizza_area > total_small_pizza_area:
    print("\nThe large pizzas provide more area than the small pizzas.")
elif total_large_pizza_area < total_small_pizza_area:
    print("\nThe small pizzas provide more area than the large pizzas.")
else:
    print("\nThe large pizzas and small pizzas provide the same area!")


# large_pizza_price = float(input("Enter the price of a single large pizza: "))
# small_pizza_price = float(input("Enter the price of a single small pizza: "))

# # total costs for large and small pizzas
# total_large_pizza_cost = num_large_pizzas * large_pizza_price
# total_small_pizza_cost = num_small_pizzas * small_pizza_price

# # comparing total costs
# print(f"\nTotal cost of {num_large_pizzas} large pizza(s): £{total_large_pizza_cost:.2f}")
# print(f"Total cost of {num_small_pizzas} small pizza(s): £{total_small_pizza_cost:.2f}")

# if total_large_pizza_cost < total_small_pizza_cost:
#     print("The large pizzas are more cost-effective.")
# elif total_large_pizza_cost > total_small_pizza_cost:
#     print("The small pizzas are more cost-effective.")
# else:
#     print("The large pizzas and small pizzas cost the same!")