# Runs through country codes, letting the user input them and check their statistics until the user inputs STOP.
# 9/7/2025
# CSC221 M1Pro – Review
# Daley Ottersbach
import Functions

allData: dict[str, dict[str, float|str]] = {
    "US": {"pop": 325.7, "gdp": 19.39, "ccy": "USD", "fx": 1.00},
    "CA": {"pop": 36.5, "gdp": 1.65, "ccy": "CAD", "fx": 1.35},
    "MX": {"pop": 129.2, "gdp": 1.15, "ccy": "MXN", "fx": 19.68},
}

if __name__ == "__main__":
    Functions.main(allData)

#### PSUEDOCODE
##
## DEFINE STRING countryCode = ""
## 
## WHILE countryCode IS NOT "STOP"
##     DISPLAY "Please enter a country code or stop: "
##     GET countryCode
##     SET countryCode = UPPER countryCode
##     IF countryCode IN a_countryInformation KEYS
##         DISPLAY "Please enter a statistic: "
##         GET statistic
##         IF statistic IN a_countryInformation[countryCode] KEYS
##             DISPLAY countryCode + " " + statistic + " = " + a_countryInformation[countryCode][statistic]
##         ELSE
##             DISPLAY "That is an invalid statistic."
##         END IF
##     ELSE IF countryCode IS "STOP"
##         DISPLAY "Terminating program."
##     ELSE
##         DISPLAY "That is an invalid country code."
##     END IF
## END WHILE
##
####