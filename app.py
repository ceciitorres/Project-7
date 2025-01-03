import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('C:/Users/cecy_/OneDrive/Documentos/Data Science/Proyectos/Project_Sprint_7/vehicles_us.csv') # leer los datos
st.header('Estadisticas de anuncios de venta de autos')
hist_button = st.button('Construir histograma') # crear un botón

        
if hist_button: # al hacer clic en el botón
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = px.histogram(car_data, x="odometer") # crear un histograma
        st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo
 
disp_button = st.button('Construir un gráfico de dispersión')     
if disp_button:
        st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        fig_disp = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig_disp, use_container_width=True)
        