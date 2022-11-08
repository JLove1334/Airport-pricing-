#Justin Love
#independent practice
#Airplane tickets
#9/26/2022

import math
def welcome():                                  #welcome the user
    print("Welcome to CSU Airlines")
    print("Tickets are $300.00 each.")
    print("Carry-on bags cost $25.00 per bag.")
    print("Checked baggages cost $55.00 per bag.")
def carry_on(carry):
    a = 25 * carry
    return a
def baggages(b):
    d = b * 55
    return d
def sales_tax(s):
    k = 0.08 * s
    return k
    
    

def main():
    #ask the user for their input
    welcome()
    c = float(input("How many carry-on bags do you have?"))
    car = carry_on(c)
    v = float(input("How many checked bags?"))
    bag = baggages(v)
    subtotal = round(300 + car + bag,2)
    tot = round(subtotal + sales_tax(subtotal),2)
    print("your subtotal is", subtotal)
    print("Your total is", tot)

main()    
              
    

    
