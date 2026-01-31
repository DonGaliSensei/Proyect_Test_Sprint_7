import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Análisis Exploratorio de Datos de Vehículos en EE.UU.")
@st.cache_data
def load_data():
    data = pd.read_csv("vehicles_us.csv")
    return data
car_data = load_data()
st.subheader("Primeras filas del dataset")
st.dataframe(car_data.head())

st.subheader("Visualizaciones")

# Botón para generar histograma
if st.button("📊 Generar Histograma de Odómetro"):
    st.write("Creando histograma...")
    
    # Crear histograma con plotly express
    fig = px.histogram(car_data, x="odometer", nbins=50, 
                       title="Distribución del Odómetro",
                       labels={"odometer": "Odómetro (km)"})
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Botón para generar gráfico de dispersión
if st.button("📈 Generar Gráfico de Dispersión"):
    st.write("Creando gráfico de dispersión...")
    
    # Crear gráfico de dispersión con plotly express
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Precio vs Odómetro",
                             labels={"odometer": "Odómetro (km)", "price": "Precio (USD)"})
    
    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

