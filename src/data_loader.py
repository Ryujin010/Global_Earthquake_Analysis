import pandas as pd


def load_data(path : str) -> pd.DataFrame:
    """
       Carga el dataset de terremotos desde un archivo CSV.
    """
    try:
        df_geh = pd.read_csv(path, encoding = 'latin-1', low_memory=False)
        print("✅ Dataset cargado correctamente\n")
        print(f'Filas : {df_geh.shape[0]}, Columnas : {df_geh.shape[1]}')
        return df_geh
    except Exception as e:
        print("❌ Error al cargar el dataset:", e)
        raise e
        #return None

if __name__ == "__main__":
    df_geh = load_data('../data/raw/earthquakes_1900_2026.csv')

    print("\nPrimeras filas: ")
    print(df_geh.head())
