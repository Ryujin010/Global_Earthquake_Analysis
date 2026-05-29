import pandas as pd

from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

def earthquakes_per_year(df_geh: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa terremotos por año.
    """

    yearly_data = (
        df_geh.groupby("year")
        .size()
        .reset_index(name="earthquake_count")
    )

    return yearly_data


def train_arima_model(series, order=(1, 1, 1)):
    """
    Entrena modelo ARIMA.
    """

    model = ARIMA(series, order=order)

    fitted_model = model.fit()

    return fitted_model


def train_auto_arima(series):
    """
    Busca Automaticamente el mejor modelo ARIMA
    """

    model = auto_arima(
        series,
        seasonal=False,
        trace=True,
        suppress_warnings=True,
        stepwise=True,
    )
    return model


def train_auto_arima_model(yearly_data : pd.DataFrame):
    """
    Entrena modelo Auto ARIMA.
    """
    model = auto_arima(
        yearly_data["earthquake_count"],
        seasonal = False,
        trace = True,
        suppress_warnings = True,
    )
    return model


def forecast_earthquakes(model, steps=10):
    """
    Genera predicciones futuras.
    """

    forecast = model.predict(n_periods = steps)

    return forecast