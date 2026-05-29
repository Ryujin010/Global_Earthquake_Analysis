import matplotlib.pyplot as plt

def plot_forecast(yearly_data_filtered, forecast_auto):
    """
    Grafica Datos Historicos + Forecast
    """

    plt.figure(figsize=(14, 6))

    # Historico
    plt.plot(
        yearly_data_filtered['year'],
        yearly_data_filtered['earthquake_count'],
        label='Historico'
    )

    # Forecast
    future_years = range(
        yearly_data_filtered['year'].max() + 1,
        yearly_data_filtered['year'].max() + 1 + len(forecast_auto)
    )

    plt.plot(
        future_years,
        forecast_auto,
        label='Forecast',
        linestyle='dashed'
    )

    plt.title('Prediccion de Terremotos para los Proximos 10 Años')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de Terremotos')
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()