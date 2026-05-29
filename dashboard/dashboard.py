import os
import sys

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# CONFIGURAR PATH DEL PROYECTO
# =========================================================

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)

# =========================================================
# IMPORTACIONES
# =========================================================

from src.data_loader import load_data
from src.cleaning import clean_data
from src.cleaning import remove_incomplete_years

from src.forecasting import (
    earthquakes_per_year,
    train_auto_arima_model,
    forecast_earthquakes
)

from src.prophet_model import (
    prepare_prophet_data,
    train_prophet_model,
    make_future_dataframe,
    predict_future
)

from src.maps import create_earthquake_map, create_depth_map

from src.feature_engineering import create_features

from src.ml_models import (
    train_random_forest_regressor,
    train_xgboost_regressor,
    regression_metrics
)

from sklearn.model_selection import train_test_split

# =========================================================
# CONFIGURACION STREAMLIT
# =========================================================

st.set_page_config(
    page_title="Global Earthquake Dashboard",
    layout="wide"
)

# =========================================================
# TITULO
# =========================================================

st.title("🌍 Global Earthquake History Dashboard")

st.markdown("---")

# =========================================================
# CARGAR DATASET
# =========================================================

df_geh = load_data("data/raw/earthquakes_1900_2026.csv")

df_geh = clean_data(df_geh)

df_geh = remove_incomplete_years(df_geh, 2025)


# =========================================================
# FEATURE ENGINEERING
# =========================================================

df_geh =create_features(df_geh)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("Filtros")

min_year = int(df_geh["year"].min())
max_year = int(df_geh["year"].max())

year_range = st.sidebar.slider(
    "Selecciona rango de años",
    min_year,
    max_year,
    (min_year, max_year)
)

min_mag = float(df_geh["mag"].min())
max_mag = float(df_geh["mag"].max())

mag_filter = st.sidebar.slider(
    "Magnitud mínima",
    min_mag,
    max_mag,
    5.0
)

# =========================================================
# FILTRAR DATASET
# =========================================================

filtered_df = df_geh[
    (df_geh["year"] >= year_range[0]) &
    (df_geh["year"] <= year_range[1]) &
    (df_geh["mag"] >= mag_filter)
]

# =========================================================
# KPIs
# =========================================================

st.subheader("📊 KPIs Globales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Terremotos",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Magnitud Promedio",
        round(filtered_df["mag"].mean(), 2)
    )

with col3:
    st.metric(
        "Profundidad Promedio",
        round(filtered_df["depth"].mean(), 2)
    )

with col4:
    top_year = (
        filtered_df["year"]
        .value_counts()
        .idxmax()
    )

    st.metric(
        "Año con más terremotos",
        int(top_year)
    )

st.markdown("---")

# =========================================================
# GRAFICO HISTORICO
# =========================================================

st.subheader("📈 Terremotos por Año")

yearly_data = earthquakes_per_year(filtered_df)

fig, ax = plt.subplots(figsize=(14, 6))

sns.lineplot(
    data=yearly_data,
    x="year",
    y="earthquake_count",
    ax=ax
)

ax.set_title("Cantidad de Terremotos por Año")
ax.set_xlabel("Año")
ax.set_ylabel("Cantidad")

plt.xticks(rotation=45)

st.pyplot(fig)

# =========================================================
# FORECAST AUTO ARIMA
# =========================================================

st.markdown("---")

st.subheader("🔮 Forecast Próximos 10 Años")

auto_model = train_auto_arima_model(yearly_data)

forecast = forecast_earthquakes(
    auto_model,
    steps=10
)

future_years = list(
    range(
        yearly_data["year"].max() + 1,
        yearly_data["year"].max() + 11
    )
)

forecast_df = pd.DataFrame({
    "year": future_years,
    "forecast": forecast.values
})

fig2, ax2 = plt.subplots(figsize=(14, 6))

# HISTORICO

sns.lineplot(
    data=yearly_data,
    x="year",
    y="earthquake_count",
    label="Histórico",
    ax=ax2
)

# FORECAST

sns.lineplot(
    data=forecast_df,
    x="year",
    y="forecast",
    label="Forecast",
    linestyle="--",
    ax=ax2
)

ax2.set_title("Predicción de Terremotos")
ax2.set_xlabel("Año")
ax2.set_ylabel("Cantidad")

plt.xticks(rotation=45)

st.pyplot(fig2)

# =========================================================
# PROPHET FORECAST
# =========================================================

st.markdown("---")

st.subheader("🤖 Prophet Forecast")

prophet_df = prepare_prophet_data(yearly_data)

prophet_model = train_prophet_model(prophet_df)

future_df = make_future_dataframe(
    prophet_model,
    periods=10
)

forecast_prophet = predict_future(
    prophet_model,
    future_df
)

fig3, ax3 = plt.subplots(figsize=(14, 6))

ax3.plot(
    prophet_df["ds"],
    prophet_df["y"],
    label="Histórico"
)

ax3.plot(
    forecast_prophet["ds"],
    forecast_prophet["yhat"],
    linestyle="--",
    label="Prophet Forecast"
)

ax3.set_title("Forecast Prophet")
ax3.set_xlabel("Fecha")
ax3.set_ylabel("Cantidad de Terremotos")

plt.xticks(rotation=45)

ax3.legend()

st.pyplot(fig3)


# =========================================================
# MACHINE LEARNING
# =========================================================
st.markdown("---")

st.subheader("🧠 Machine Learning")

features = [
    "depth",
    "latitude",
    "longitude",
    "year"
]

target = "mag"

X = filtered_df[features]

y = filtered_df[target]

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================================================
# RANDOM FOREST
# =========================================================

rf_model = train_random_forest_regressor(
    X_train,
    y_train
)

rf_metrics = regression_metrics(
    rf_model,
    X_test,
    y_test
)

# =========================================================
# XGBOOST
# =========================================================

xgb_model = train_xgboost_regressor(
    X_train,
    y_train
)

xgb_metrics = regression_metrics(
    xgb_model,
    X_test,
    y_test
)

# =========================================================
# METRICAS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌲 Random Forest")

    st.write(rf_metrics)

with col2:

    st.subheader("🚀 XGBoost")

    st.write(xgb_metrics)

# =========================================================
# MAPA GLOBAL
# =========================================================

st.markdown("---")

st.subheader("🌍 Global Earthquake Map")

map_df = filtered_df.sample(
    min(5000, len(filtered_df))
)

earthquake_map = create_earthquake_map(
    map_df
)

st.plotly_chart(
    earthquake_map,
    use_container_width=True
)

# =========================================================
# MAPA PROFUNDIDAD
# =========================================================

st.markdown("---")

st.subheader("🌊 Earthquake Depth Map")

depth_map = create_depth_map(
    map_df
)

st.plotly_chart(
    depth_map,
    use_container_width=True
)


# =========================================================
# TABLA DE PREDICCIONES
# =========================================================

st.markdown("---")

st.subheader("📋 Predicciones Futuras")

st.dataframe(forecast_df)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    Dashboard desarrollado con las siguientes tecnologias :
    
    - Python
    - Streamlit
    - Pandas
    - Seaborn
    - Scikit-Learn
    - XGBoost
    - Prophet
    - Plotly
    - ARIMA
    """
)