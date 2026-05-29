import pandas as pd


def clean_data(df_geh: pd.DataFrame) -> pd.DataFrame:
    """
    Limpieza general del dataset de terremotos.
    """

    # Normalizar nombres de columnas
    df_geh.columns = df_geh.columns.str.strip().str.lower()

    # Eliminar nulos críticos
    df_geh = df_geh.dropna(subset=["mag", "depth"])

    # Validar magnitud
    df_geh = df_geh[
        (df_geh["mag"] > 0) &
        (df_geh["mag"] <= 10)
    ]

    # Validar profundidad
    df_geh = df_geh[
        df_geh["depth"] >= 0
    ]

    # Validar coordenadas geográficas
    df_geh = df_geh[
        (df_geh["latitude"].between(-90, 90)) &
        (df_geh["longitude"].between(-180, 180))
    ]

    # Convertir año a entero
    df_geh["year"] = df_geh["year"].astype(int)

    # Eliminar duplicados
    df_geh = df_geh.drop_duplicates()

    return df_geh


def remove_incomplete_years(
        #yearly_data: pd.DataFrame,
        df_geh,
        #last_valid_year: int
        last_valid_year: 2025,
): # -> pd.DataFrame:
    """
    Elimina años incompletos para forecasting.
    """

    #filtered_df = yearly_data[
    #    yearly_data["year"] <= last_valid_year
    #]
    filtered_df = df_geh[
        df_geh["year"] <= last_valid_year
    ]

    return filtered_df