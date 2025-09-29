# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:58:04 2024

@author: seidih6290
"""


from m2Lab_classes import Customer
import csv
    
def menu() -> None:
    #Display the header
    print("Menu\n----------------\n1. Display Customer Dataset\n2. Add Customer\n3. Update Customer Info\n4. Exit Program and Generate Customer Files")

def get_cusInfo() -> list[Customer]:
    '''
    function read csv file of customers and creates Customer Instances
    Returns
    -------
    customers : List of Customer Instances.

    '''
    customers: list[Customer] = []
    
    try:
        with open("customer.csv") as customer_file:
            customer_file_csv = csv.reader(customer_file)
            # skip first row
            next(customer_file_csv)
            for row in customer_file_csv:
                first, last, phone, email, state, address = row
                # create instance and add to list
                customer: Customer = Customer(first, last, phone, email, address,state )
                customers.append(customer)
    except FileNotFoundError:
        print("File Error! Customer File Not Found!") #Throw an error if the file is not found
    
    return customers
    
def cus_update(lastName: str, customers: list[Customer]) -> list[Customer]:

    found: bool = False 
                
    for cus in customers:
        cus_last: str = cus.get_last()
        
        # check if instance last name is same as one we want to update
        if cus_last == lastName: # customer found in list
            # ask user to choose from update options
            print("\nWhat would you like to update? \n\n1) Update Phone\n2) Update Address")
            
            option: int = int(input("Enter choice: "))

            # see option picked
            if option == 1: # update phone
                # display old phone number
                print(f"\n{cus.get_first()} {cus_last} current phone number is {cus.get_phone()}")
                
                # get new phone number
                phone: str = input(f"What is {cus.get_first()} {cus_last}\'s new phone number: ")
                
                # update the phone
                cus.set_phone(phone)
                # show new information to user
                print("\nPhone number updated, see below\n\n{cus.get_first()} {cus_last} updated phone number is {cus.get_phone()}")
                
                return customers # return updated customers list
            elif option == 2: # update address
                # display old address
                print(f"\n{cus.get_first()} {cus_last} current address is {cus.get_address()}")
                
                # ask if moving to new state
                move: str = input(f"Will {cus.get_first()} {cus_last} be moving to a new state(y for yes): ")
                
                if move.lower() =='y':
                    # get state
                    state: str = input(f"Enter the state {cus.get_first()} {cus_last} will move to: ")     
                
                    # get new address
                    address: str = input(f"What is {cus.get_first()} {cus_last}\'s new address: ")
                    
                    #update
                    cus.set_state(state)
                    cus.set_address(address)
                    
                    return customers
                else: # only update address 
                    # get new address
                    address: str = input(f"What is {cus.get_first()} {cus_last}\'s new address: ")
                    
                    #update
                    cus.set_address(address)
                return customers
            else:
                print("Invalid option picked!!!")
    # if last name not found
    if not found:
        print(f"\n{lastName} does not exit in list of customers!!")
    return customers