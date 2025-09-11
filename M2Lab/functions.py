import pandas
import numpy

def FindDifference(a_snpData: pandas.DataFrame, a_priceData: pandas.DataFrame) -> pandas.DataFrame:
    """Adds a differnece column to a pandas dataframe with date columns.
    
    Args:
        a_snpData (DataFrame): A DataFrame containing the full data.
        a_priceData (DataFrame): A DataFrame containing the price data, dates, and symbols.

    Returns:
        (DataFrame): The modified DataFrame.
    """
    dataHolder: dict[str, list[float]] = {}

    for row in a_snpData.transpose():
        for col in a_priceData:
            dataHolder[row] = dataHolder.get(row, []) + ([a_priceData[col][row]] if row in a_priceData[col] and not numpy.isnan(a_priceData[col][row]) else [])
    
    a_snpData["difference"] = a_snpData.apply(lambda r: dataHolder[r.name][-1] - dataHolder[r.name][-2] if len(dataHolder[r.name]) > 1 else None, axis=1)

    return a_snpData


#### Psuedocode
## Set dataHolder to {}
## Foreach row in a_snpData transposed
##   Foreach col in a_priceData
##     Set dataHolder[row] to dataHolder get row or default to [] concatenated with a_priceData of row is in a_priceData[col] and a_priceData[col][row] is not NaN, else []
##   End Foreach
## End Foreach
## Set a_snpData["difference"] to the difference between the price on the last available date and the price on the prior available date fo every row
## Return a_snpData