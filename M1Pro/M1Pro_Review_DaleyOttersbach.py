# IDK
# 8/28/2025
# CSC221 M1Pro – Review
# Daley Ottersbach

allData = {
    "US": {"pop": 325.7, "gdp": 19.39, "ccy": "USD", "fx": 1.00},
    "CA": {"pop": 36.5, "gdp": 1.65, "ccy": "CAD", "fx": 1.35},
    "MX": {"pop": 129.2, "gdp": 1.15, "ccy": "MXN", "fx": 19.68},
}


def main() -> None:
    running: bool = True
    while running:
        countryCode: str = input("Please enter a country code or stop: ").upper()
        if countryCode in allData.keys():
            statistic: str = input("Please enter a statistic: ").lower()
            if statistic in allData[countryCode].keys():
                print(f"{countryCode} {statistic} = {allData[countryCode][statistic]}")
            else:
                print("That is an invalid statistic.")
        elif countryCode == "STOP":
            print("Terminating program.")
            running = False
        else:
            print("That is an invalid country code.")


if __name__ == "__main__":
    main()

