


#Create the subclass Contact
#Initialize new attributes for the class
#Define setters and getters
#Create the menu 
#Set up a try catch to Read the csv file content and create instances
#Write contact information into a txt file  and display contact text file to the user


import con_func as fn
from m2Lab_classes import Customer
import pandas as pd
  

def main() -> None:
    # call function that reads csv file and creates instances
    customers: list[Customer] = fn.get_cusInfo() # list references Customer instances
    
    
    #Create the main loop which will keep the program running until the user exits
    choice: int = 0
    while choice != 4: # not exit
        # display menu
        fn.menu()
        choice = int(input("Please enter an option : "))
        
        if choice == 1: # display instances
            # read instaces from list and display 
            for cus in customers:
                print(cus)
        elif choice == 2: # add customer
            # Ask for number of customers to be added
            num = int(input("How many customers would you like to add: "))
            
            # get info
            for cus_num in range(1, num + 1):
                print("\nCustomer",cus_num,"Info:")
                
                first: str = input(f"Enter first name for customer# {cus_num} : ")
                last: str = input(f"Enter last name for customer# {cus_num} : ")
                phone: str = input(f"What is {first} {last}\'s phone number: ")
                email: str = input(f"What is {first} {last}\'s email: ")
                state: str = input(f"In what state does {first} {last} live: ")
                address: str = input(f"Enter {first} {last}\'s address? ")
                
                # add to cumstomers list
                customers.append(Customer(first,last,phone, email, state, address))
                # Notify that customer has been added
                print("\nCustomer Instance Created")
        elif choice == 3: # update custoemr info
            # ask user for customer last name
            last = input("Enter customer's last name: ")
            
            #call the update function
            customers = fn.cus_update(last, customers)
        elif choice == 4: # Create reports and exit
            # create new csv file of customers
            # first create a dataFrame from list of instances
            # Extract data from instances
            
            # create the dataFrame
            customerPD = pd.DataFrame([{
                    'FirstName': cus.get_first(),
                    'lastName': cus.get_last(),
                    'Phone#': cus.get_phone(),
                    'State': cus.get_state(),
                    'Address': cus.get_address()
                } for cus in customers
            ])
            # now write to csv
            customerPD.to_csv("customers_updated.csv",  index=False)
            #notify user
            print("\ncustomers_updated.csv has been created(contains updated customer info)\n\nClosing program! Good bye.")
        else:
            # if anything other than 1 - 4 is inputed give an error
            print("This is not a valid option! Please choose from the menu. /n\n")
    
if __name__ == "__main__":
    main()