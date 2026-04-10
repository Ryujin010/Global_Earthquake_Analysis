def clean_data(df_geh):
    df_geh.columns = df_geh.columns.str.strip().str.lower()

    df_geh = df_geh.dropna(subset=["mag", "depth"])

    df_geh = df_geh[(df_geh["mag"] > 0) & (df_geh["mag"] <= 10)]
    df_geh = df_geh[df_geh["depth"] >= 0]

    df_geh = df_geh[
        (df_geh["latitude"].between(-90, 90)) &
        (df_geh["longitude"].between(-180, 180))
    ]

    df_geh["year"] = df_geh["year"].astype(int)

    return df_geh