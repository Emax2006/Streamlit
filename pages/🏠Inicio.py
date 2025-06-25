import streamlit as st
import pandas as pd
from data_manager import load_data

# Cargar archivo automáticamente
ruta_archivo = r"C:\Users\SENA\Music\archive\used_car_price_dataset_extended.csv"

try:
    df = pd.read_csv(ruta_archivo)
    load_data(df)
except Exception as e:
    st.error(f"No se pudo cargar el archivo automáticamente: {e}")

# Diseño de la página
st.markdown("""
    <style>
        .titulo {
            font-size: 36px;
            font-weight: bold;
            color: #1a237e;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .descripcion {
            font-size: 18px;
            text-align: center;
            color: #FFFFFF;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>🚗 Sistema de Análisis y Predicción de Accidentes Vehiculares</div>", unsafe_allow_html=True)
st.markdown("<div class='descripcion'>Este sistema permite analizar datos reales de vehículos usados y predecir su propensión a accidentes, además de ofrecer visualizaciones automáticas y estadísticas clave del dataset cargado.</div>", unsafe_allow_html=True)

# Mostrar imágenes en dos columnas
col1, col2 = st.columns(2)

with col1:
    st.image("images/3558c7e5-e00b-4a08-9da8-46752522e8fc.png", caption="BMW 8 Series", use_container_width=True)
    st.image("images/0f0bdead-28e2-410a-9534-fc1055641612.png", caption="Nissan GTR", use_container_width=True)

with col2:
    st.image("images/945df8e4-2b01-4472-9359-1e33be5d0cb0.png", caption="Tesla Model Y", use_container_width=True)
    st.image("images/d0d2599a-8cef-4dbb-953c-eaee1175319c.png", caption="Toyota Supra", use_container_width=True)
