Introduction:
Assignment requires using all the skills learn to this point. Since the program will also require using sql commands to retrieve information from tables, a concepts not required for this class, students can consider using AI if needed

Instructions:
This assignment requires reading and evaluating database content. The database you are to work on for this assignment is linked on in the assignment post on Bb ( name of sqlite database is �vet_serv.db�). make sure you download the database and save it in the project folder.

About the Database.
The program you will create is going to retrieve information from the database you were provided. However, in order to retrieve information from a database, we need to know several things:
* The tables it contains, what are they named
* The fields in each table
* What is the Primary key assigned for each table
* How are the tables linked (Foreign keys)

Below is the information for the database you will work on.
* There are Two tables in the database (OWNER, PETS).
* OWNER table fields
    * (OwnerId, OwnerLastName, OwnerFirstName, OwnerPhone, OwnerEmail)
    * The primary key is OwnerId
* PETS table fields 
    * (PetId,PetName,PetType,PetBreed,PetDOB,Service	,Date,Charge,OwnerId)
    * Primary key is PetId
    * Foreign key is OwnerId
* The two tables are linked via the Foreign key OwnerId
* Last but not least , the purpose of the database is to track pet and owner information at a veterinary clinic

What will the program do?
Create a program that does the following.
1. Reads the database you downloaded. 
2. The program will be menu driven , you should be used to this by now ?? . After reading the database, the program is to display the following menu
    1.  Display OWNER content and create DataFrame
    2. Display PETS content and create DataFrame
    3. Retrieve Owner and Pet data for specific Owner
    4. Calculate Total Charge by Owner
    5. Retrieve Pet information by PetBreed
    6. Exit

If option 1 is selected :
* Read all fields and content in the OWNER table into a DataFrame.
* Display the DataFrame created.
* Write DataFrame content into a csv file. Name the file `owner.csv`

If option 2 is selected:
* Read all fields and content in the PETS table into a DataFrame.
* Display the DataFrame created.
* Write DataFrame content into a csv file. Name the file `pets.csv`

If option 3 is selected:
* Prompt the user to enter OwnerId
* Retrieve and display all records (from BOTH tables) that pertain to that Owner. Fields you need to retrieve are as following (OwnerId, OwnerFirstName, OwnerLastName, OwnerPhone, OwnerEmail ,PetId, PetName, PetBreed, PetDOB)
* Write the information retrieved into a csv file. The file name depends on the owner search . For instance if the ownerId entered was 4001 and the owner last name was Smith, the file is to be named  `smith_4001.csv`

If option 4 is selected:
* Prompt the user to enter OwnerId
* Retrieve and display all records (from BOTH tables) that pertain to that Owner. Fields you need to retrieve are as following (OwnerId, OwnerFirstName, OwnerLastName, OwnerEmail ,PetId, PetName, PetBreed, Service, Date, Charge)
* Calculate the total charge, sum of charges (some owners might have brought in more than one pet ).
* After displaying the information retrieved, display the sum of charges for the owner

If option 5 is selected:
You will need to use DataFrame features and methods in this option
* Read the PETS table into a DataFrame.
* Prompt the user to enter PetBreed they want to research
* Retrieve all records that reference the PetBreed entered.
* Display the total charges and overall average for the PetBreed entered.

If option 6 is selected:
Display a message notifying the user that the program will terminate. The program is to stop after displaying the message.

If different option selected:
Display a message notifying the user that they have picked an invalid option and display the menu again.
