import pandas as pd

from prophet import Prophet


def prepare_prophet_data(
        yearly_data: pd.DataFrame
) -> pd.DataFrame:
    """
    Convierte datos al formato requerido por Prophet.
    """

    prophet_df = yearly_data.copy()

    prophet_df = prophet_df.rename(
        columns={
            "year": "ds",
            "earthquake_count": "y"
        }
    )

    prophet_df["ds"] = pd.to_datetime(
        prophet_df["ds"].astype(str),
        format="%Y"
    )

    return prophet_df


def train_prophet_model(
        prophet_df: pd.DataFrame
):
    """
    Entrena modelo Prophet.
    """

    model = Prophet()

    model.fit(prophet_df)

    return model


def make_future_dataframe(
        model,
        periods=10
):
    """
    Genera años futuros.
    """

    future = model.make_future_dataframe(
        periods=periods,
        freq="YE"
    )

    return future


def predict_future(model, future_df):
    """
    Generar Predicciones Futuras
    """
    forecast = model.predict(future_df)
    return forecast


def generate_forecast(
        model,
        future_df
):
    """
    Genera forecast Prophet.
    """

    forecast = model.predict(
        future_df
    )

    return forecast