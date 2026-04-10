import matplotlib.pyplot as plt
import seaborn as sns

# Histograma de Distribucion de Magnitudes

def plot_magnitude_distribution(df_geh):
    plt.figure(figsize=(10, 5))
    sns.histplot(df_geh['mag'], bins=50)
    plt.title('Distribucion de Magnitudes')
    plt.xlabel('Magnitude')
    plt.ylabel('Cantidad de eventos')
    plt.show()

    plt.savefig("reports/figures/magnitude_distribution.png")
    plt.close()

# Grafica de Caja de Outliers

def plot_outliers_magnitude(df_geh):
    plt.figure(figsize=(8, 4))
    sns.boxplot(x = df_geh['mag'])
    plt.title('Outliers en Magnitud')
    plt.xlabel('Magnitud del Evento')
    plt.show()

    plt.savefig("reports/figures/outliers_magnitude.png")
    plt.close()

# Grafica con Outliers por Magnitud de Evento .

def plot_outliers_distribution(df_geh):
    # Filtrar Valores Irreales de Magnitud.
    df_geh = df_geh[(df_geh['mag'] > 0) & (df_geh['mag'] <= 10)]

    # Filtrar Valores de Profundidad
    df_geh = df_geh[df_geh['depth'] > 0]

    # Visualizacion de Outliers

    plt.figure(figsize=(12,6))
    sns.boxplot(x = df_geh['mag'], y = df_geh['depth'])
    plt.scatter(df_geh['longitude'], df_geh['latitude'], alpha = 0.3)
    plt.title('Distribucion de Magnitudes y Profundidad')
    plt.xlabel('Magnitud')
    plt.ylabel('Profundidad')
    plt.show()

    plt.savefig("reports/figures/outliers_distribution.png")
    plt.close()

# Grafica de Terremotos por año.

def plot_earthquakes_per_year(df_geh):
    earthquakes_per_year = df_geh.groupby("year").size().sort_index()

    plt.figure(figsize=(12,5))
    earthquakes_per_year.plot()
    plt.title("Número de terremotos por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de eventos")
    plt.show()

    plt.savefig("reports/figures/earthquakes_per_year.png")
    plt.close()

# Grafica de la Tendencia de Terremotos a cada 5 Años

def plot_earthquakes_per_5_years(df_geh):
    earthquakes_per_5_years = df_geh.groupby("year").size().sort_index()

    earthquakes_per_5_years.rolling(5).mean().plot(figsize = (12, 5))
    plt.xlabel('Años')
    plt.title('Tendencia de Terremotos (Media Movil cada 5 Años)')
    plt.show()

    plt.savefig("reports/figures/earthquakes_per_5_years.png")
    plt.close()


# Grafica de los Años con mas Terremotos.

def plot_years_most_earthquakes(df_geh):
    earthquakes_per_year = df_geh.groupby("year").size().sort_index()

    anios_mas_terremotos = earthquakes_per_year.sort_values(ascending = False)
    #añios_mas_terremotos.head(10)

    plt.figure(figsize=(10, 5))
    sns.barplot(anios_mas_terremotos.head(15))
    plt.xlabel('Año')
    plt.ylabel('Cantidad de eventos')
    plt.title('Años con mas Terremotos')
    plt.show()

    plt.savefig("reports/figures/years_most_earthquakes.png")
    plt.close()

# Grafica de Terremotos por Mes.

def plot_earthquakes_per_month(df_geh):
    earthquakes_per_month = df_geh.groupby("month").size().sort_index()

    earthquakes_per_month.plot(figsize=(12,5))
    plt.xlabel('M E S')
    plt.ylabel('Cantidad de eventos')
    plt.title('Terremotos por Mes')
    plt.show()

    plt.savefig("reports/figures/earthquakes_per_month.png")
    plt.close()

# Grafica con la Ubicacion de los Terremotos.

def plot_geographical_distribution(df_geh):
    plt.figure(figsize=(10,6))
    plt.scatter(df_geh['longitude'], df_geh['latitude'], alpha = 0.3)
    plt.title('Ubicacion de Terremotos')
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.show()

    plt.savefig("reports/figures/geographical_distribution.png")
    plt.close()

# Relacion Magnitud Vs Profundidad

def plot_magnitude_vs_depth_relationship(df_geh):
    plt.figure(figsize=(10,5))
    sns.scatterplot(x = df_geh["depth"], y = df_geh["mag"], alpha=0.3)
    plt.title("Magnitud vs Profundidad")
    plt.xlabel('Profundidad')
    plt.ylabel('Magnitud')
    plt.show()

    plt.savefig("reports/figures/magnitude_vs_depth.png")
    plt.close()