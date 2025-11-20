def intput(a_prompt: str) -> int:
    """Get an int formated input.
    
    Args:
        a_prompt (str): The prompt to display.
    
    Returns:
        out (int): The input value.
    """
    try:
        return int(input(a_prompt))
    except Exception as e:
        #print(e)
        return intput(a_prompt)
    
def displayOptions() -> None:
    """Display the options.
    """
    print("Options:\n1) Display OWNER content\n2) Display PETS content\n3) Retrieve Owner and Pet data for specific Owner\n4) Calculate Total Charge by Owner\n5) Retrieve Pet information by PetBreed\n6) Exit\n")
