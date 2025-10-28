import sqlite3 as sql
from sqlite3 import Connection, Cursor
import pandas as pd
from pandas import DataFrame

from functions import intput

"""
* OWNER table
    * (OwnerId, OwnerLastName, OwnerFirstName, OwnerPhone, OwnerEmail)
    * The primary key is OwnerId
* PETS table
    * (PetId, PetName, PetType, PetBreed, PetDOB, Service, Date, Charge, OwnerId)
    * Primary key is PetId
    * Foreign key is OwnerId
"""

def displayOptions() -> None:
    """Display the options.
    """
    print("Options:\n1) Display OWNER content\n2) Display PETS content\n3) Retrieve Owner and Pet data for specific Owner\n4) Calculate Total Charge by Owner\n5) Retrieve Pet information by PetBreed\n6) Exit\n")

def main() -> None:
    """Main function.
    """
    connection: Connection = sql.connect("vet_serv.db")
    cursor: Cursor = connection.cursor()
    result = cursor.execute("""SELECT OwnerId, OwnerLastName, OwnerFirstName, OwnerPhone, OwnerEmail FROM OWNER""")
    owners: DataFrame = DataFrame.from_records(result.fetchall(), columns=["OwnerID", "OwnerLastName", "OwnerFirstName", "OwnerPhone", "OwnerEmail"]).set_index("OwnerID")
    result = cursor.execute("""SELECT PetId, PetName, PetType, PetBreed, PetDOB, Service, Date, Charge, OwnerId FROM PETS""")
    pets: DataFrame = DataFrame.from_records(result.fetchall(), columns=["PetID", "PetName", "PetType", "PetBreed", "PetDOB", "Service", "Date", "Charge", "OwnerID"]).set_index("PetID")
    
    option: int = -1
    while option != 6:
        displayOptions()
        match (option := intput("Choice: ")):
            case 1:
                print(owners)
                owners.to_csv("owner.csv")
            case 2:
                print(pets)
                pets.to_csv("pets.csv")
            case 3:
                result = cursor.execute(f"""SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, OWNER.OwnerPhone, OWNER.OwnerEmail, PETS.PetId, PETS.PetName, PETS.PetBreed, PETS.PetDOB FROM OWNER, PETS WHERE OWNER.OwnerId=PETS.OwnerId AND OWNER.OwnerId='{(ownerID := intput("OwnerID (xxxx): "))}'""")
                ownersPets: DataFrame = DataFrame.from_records(result.fetchall(), columns=["OwnerID", "OwnerFirstName", "OwnerLastName", "OwnerPhone", "OwnerEmail", "PetID", "PetName", "PetBreed", "PetDOB"]).set_index(["OwnerID", "PetID"])
                print(ownersPets)
                ownersPets.to_csv(f"{owners.loc[ownerID].OwnerLastName.lower()}_{ownerID}.csv")
            case 4:
                result = cursor.execute(f"""SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, OWNER.OwnerEmail, PETS.PetId, PETS.PetName, PETS.PetBreed, PETS.Service, PETS.Date, PETS.Charge FROM OWNER, PETS WHERE OWNER.OwnerId=PETS.OwnerId AND OWNER.OwnerId='{(ownerID := intput("OwnerID (xxxx): "))}'""")
                ownersPets: DataFrame = DataFrame.from_records(result.fetchall(), columns=["OwnerID", "OwnerFirstName", "OwnerLastName", "OwnerEmail", "PetID", "PetName", "PetBreed", "Service", "Date", "Charge"]).set_index(["OwnerID", "PetID"])
                print(ownersPets)
                print(f"Total Charge: ${ownersPets.loc[ownerID].loc[:,"Charge"].sum():.2f}")
            case 5:
                petBreed: str = input("Pet Breed: ")
                print(pets.loc[pets.PetBreed == petBreed])
                print(f"Total Charge: ${pets.loc[pets.PetBreed == petBreed,"Charge"].sum():.2f}\nAverage Charge: ${pets.loc[pets.PetBreed == petBreed,"Charge"].mean():.2f}")
            case 6:
                print("Terminating.")
            case _:
                print(f"{option} is an invalid choice.")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()