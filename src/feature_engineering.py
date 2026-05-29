import pandas as pd

# =========================================================
# RISK CATEGORY
# =========================================================

def create_risk_category(df_geh : pd.DataFrame):
    """
    Crear Categorias de Riesgo
    """

    def classify_risk(mag):
        if mag <= 4:
            return "LOW"
        elif mag <= 6:
            return "MEDIUM"
        elif mag <= 8:
            return "HIGH"
        else:
            return "XTREME"


    df_geh["risk_level"] = (
        df_geh["mag"].apply(classify_risk)
    )

    return df_geh

# =========================================================
# DEPTH CATEGORY
# =========================================================

def create_depth_category(df_geh : pd.DataFrame):
    """
    Categorizar la Profundidad del Evento
    """
    def classify_depth(depth):
        if depth <= 70:
            return "SHALLOW"
        elif depth <= 300:
            return "INTERMEDIATE"
        else:
            return "DEEP"

    df_geh["depth_category"] = (
        df_geh["depth"].apply(classify_depth)
    )

    return df_geh


# =========================================================
# HEMISPHERE FEATURE
# =========================================================

def create_hemisphere_feature(df_geh : pd.DataFrame):
    """
    Crear Hemisferio Geografico de los Eventos
    """

    df_geh["hemisphere"] = (
        df_geh["latitude"].apply(
            lambda x : "North"
            if x >= 0
            else "South"
        )
    )

    return df_geh


# =========================================================
# MAIN FEATURE ENGINEERING
# =========================================================

def create_features(df_geh : pd.DataFrame):
    """
    Pipeline principal de Features Engineering
    """

    # Riesgo Sismico

    df_geh = create_risk_category(df_geh)

    # Profundidad

    df_geh = create_depth_category(df_geh)

    # Hemisferio

    df_geh = create_hemisphere_feature(df_geh)

    return df_geh