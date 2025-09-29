class Person:
    def __init__(self, first: str, last: str, phone: str):
        self.__first: str = first
        self.__last: str = last
        self.__phone: str = phone

    def set_first(self, name: str) -> None:
        self.__first = name

    def set_last(self, last: str) -> None:
        self.__last = last

    def set_phone(self, phone: str) -> None:
        self.__phone = phone
    
    def get_first(self) -> str:
        return self.__first
        
    def get_last(self) -> str:
        return self.__last
    
    def get_phone(self) -> str:
        return self.__phone
    
    def __repr__(self) -> str:
        return f'{self.__first:<20}{self.__last:<20}{self.__phone:<20}'

class Customer(Person):
    def __init__(self, first: str, last: str, phone: str, email: str, state: str, address: str):
        super().__init__(first, last, phone)
        self.__email: str = email
        self.__state: str = state
        self.__address: str = address
     
    #Setters
    def set_email(self, email: str) -> None:
        self.__email = email

    def set_address(self, address: str) -> None:
        self.__address = address

    def set_state(self, state: str) -> None:
        self.__state = state
  
    #Getters   
    def get_email(self) -> str:
        return self.__email

    def get_address(self) -> str:
        return self.__address
    
    def get_state(self) -> str:
        return self.__state
    
    def __repr__(self) -> str:
        return f"{Person.__repr__(self)}{self.__address:<20}{self.__state:<20}"
  
        




