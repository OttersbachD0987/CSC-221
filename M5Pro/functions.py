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