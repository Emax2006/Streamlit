import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_manager import get_data

st.title("📊 Análisis Gráfico Automático")

df = get_data()

if df is not None:
    st.subheader("1️⃣ Distribución de Marcas")
    fig1, ax1 = plt.subplots()
    df['brand'].value_counts().plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_xlabel("Marca")
    ax1.set_ylabel("Cantidad")
    ax1.set_title("Cantidad de Vehículos por Marca")
    st.pyplot(fig1)

    st.subheader("2️⃣ Distribución del Año de Fabricación")
    fig2, ax2 = plt.subplots()
    df['make_year'].value_counts().sort_index().plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.set_xlabel("Año")
    ax2.set_ylabel("Cantidad de Vehículos")
    ax2.set_title("Vehículos por Año de Fabricación")
    st.pyplot(fig2)

    st.subheader("3️⃣ Relación entre Precio y Cilindraje")
    if 'price_usd' in df.columns and 'engine_cc' in df.columns:
        fig3, ax3 = plt.subplots()
        sns.scatterplot(data=df, x='engine_cc', y='price_usd', hue='brand', ax=ax3)
        ax3.set_xlabel("Cilindraje (cc)")
        ax3.set_ylabel("Precio (USD)")
        ax3.set_title("Relación entre Cilindraje y Precio")
        st.pyplot(fig3)
    else:
        st.warning("No se encontraron columnas 'price_usd' y 'engine_cc' para este gráfico.")

    st.subheader("4️⃣ Accidentes reportados por Marca")
    if 'accidents_reported' in df.columns:
        fig4, ax4 = plt.subplots()
        accidentes = df.groupby('brand')['accidents_reported'].sum().sort_values(ascending=False)
        accidentes.plot(kind='bar', ax=ax4, color='coral')
        ax4.set_xlabel("Marca")
        ax4.set_ylabel("Total de Accidentes Reportados")
        ax4.set_title("Accidentes Reportados por Marca")
        st.pyplot(fig4)
    else:
        st.warning("La columna 'accidents_reported' no está disponible para graficar.")
else:
    st.warning("Por favor, carga primero los datos en la página de Inicio.")
