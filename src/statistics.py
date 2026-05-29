from statsmodels.tsa.stattools import adfuller

def adf_test(series):
    """
    Augmented Dickey-Fuller Test (ADF)
    """
    result = adfuller(series)

    print("ADF Statistics:", result[0])
    print("p-value:", result[1])

    if result[1] < 0.05:
        print("La Serie es Estacionaria")
    else:
        print("La serie NO es Estacionaria")
