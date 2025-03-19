# Write a program to work out the amount of change from, say, a vending machine.
# The program should prompt for the total amount the item cost (in pence), 
# and the amount a customer has put in the machine (also in pence).

# It should then display the amount of change that should be dispensed.


#!/usr/bin/env python3

def vending():

    cost = int(input("Enter the total cost of the item (in pence): "))
    paid = int(input("Enter the amount paid (in pence): "))
    
    if paid < cost:
        print("Insufficient amount! Put more to get the items.")
    else:
        change_given = paid - cost
        print(f"The change to be dispensed is: {change_given} pence.")

# Run the function
if __name__ == '__main__':
    
    vending()