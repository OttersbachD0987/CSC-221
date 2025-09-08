def main(a_countryInformation: dict[str, dict[str, float|str]]) -> None:
    """Runs a loop to handle country codes and statistics of them. Exits on STOP input.

    Args:
        a_countryInformation (dict[str, dict[str, float|str]]): a
    """
    countryCode: str = ""
    while countryCode != "STOP":
        countryCode: str = input("Please enter a country code or stop: ").upper()
        if countryCode in a_countryInformation.keys():
            statistic: str = input("Please enter a statistic: ").lower()
            if statistic in a_countryInformation[countryCode].keys():
                print(f"{countryCode} {statistic} = {a_countryInformation[countryCode][statistic]}")
            else:
                print("That is an invalid statistic.")
        elif countryCode == "STOP":
            print("Terminating program.")
        else:
            print("That is an invalid country code.")