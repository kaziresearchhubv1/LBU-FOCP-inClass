
# Write a short program that prompts the user to enter an amount of money in £s, 
# and displays the equivalent amount in $s.

# Hint: £1 is currently about $1.30.
# Remember to program the "Happy Path" first, and then worry about errors.


#!/usr/bin/env python3

if __name__ == '__main__':

    money_pound = float(input("Enter your amount in GBP: £"))

    money_dollar = money_pound*1.30

    print (f"Requested £{money_pound} is equuivalent to ${money_dollar}. Thanks!!")