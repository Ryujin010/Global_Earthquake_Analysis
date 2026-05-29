import plotly.express as px


def create_earthquake_map(df_geh):
    """
    Crear un Mapa Mundial Interactivo
    """

    fig = px.scatter_geo(
        df_geh,
        lat = "latitude",
        lon = "longitude",
        color = "mag",
        size = "mag",
        hover_name = "place",
        projection = "natural earth",
        title = "Mapa Global de Terremotos",
        color_continuous_scale = "Turbo"
    )

    return fig


def create_depth_map(df_geh):

    fig = px.scatter_geo(
        df_geh,
        lat = "latitude",
        lon = "longitude",
        color = "depth",
        size = "mag",
        hover_name = "place",
        projection = "natural earth",
        title = "Mapa de Profundidad de Terremotos",
        color_continuous_scale = "Viridis"
    )

    return fig