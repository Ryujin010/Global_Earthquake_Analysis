import streamlit as st
import pandas as pd

#from notebooks.eda import earthquakes_per_year
from src.data_loader import load_data
from src.cleaning import clean_data

# Configuracion
st.set_page_config(page_title="Earthquake Dashboard", layout = "wide")

st.title("🌍 Global Earthquake Dashboard")

# Cargar Datos
df_geh = load_data(path = "./data/raw/earthquakes_1900_2026.csv")
df_geh = clean_data(df_geh)

# Sidebat (Filtros)
st.sidebar.header('Filtros')

year_range = st.sidebar.slider(
    'Selecciona el Rango de Años',
    int(df_geh['year'].min()),
    int(df_geh['year'].max()),
    (2000, 2020)
)

min_magnitude = st.sidebar.slider(
    'Magnitud Minima',
    float(df_geh['mag'].min()),
    float(df_geh['mag'].max()),
    4.5
)

# Aplicar Filtros

df_geh_filtered = df_geh[
    (df_geh['year'].between(year_range[0], year_range[1])) &
    (df_geh['mag'] >= min_magnitude)
]

# Mostrar Datos

st.subheader('Datos Filtrados')
st.write(df_geh_filtered.head())

# Grafica 1
st.subheader('Terremotos por Año')

earthquakes_per_years = df_geh_filtered.groupby('year').size()

st.line_chart(earthquakes_per_years)

# Grafica 2
st.subheader('Distribucion de Magnitudes')

st.bar_chart(df_geh_filtered['mag'].value_counts().sort_index())

# Mapa
st.subheader('Mapa de Terremotos')

st.map(df_geh_filtered[['latitude', 'longitude']].dropna())

# KPIs
st.subheader('KPIs')
st.metric('Total de Terremotos', len(df_geh_filtered))
st.metric('Magnitud Promedio', round(df_geh_filtered['mag'].mean(), 2))

# Filtros por Ubicacion
country = st.sidebar.selectbox('Pais', df_geh['place'].unique())