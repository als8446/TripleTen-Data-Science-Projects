import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Explorando los anuncios de venta de coches")

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox('Mostrar gráfico de dispersión')
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el precio vs millaje')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre millaje y precio")
    st.plotly_chart(fig, use_container_width=True)


