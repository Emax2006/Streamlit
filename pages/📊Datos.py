import streamlit as st
import pandas as pd
from data_manager import get_data

st.title("📄 Visualización de Datos")

df = get_data()

if df is not None:
    st.subheader("📌 Información General del Dataset")

    # Tamaño
    st.write(f"🔢 **Filas:** {df.shape[0]} | **Columnas:** {df.shape[1]}")

    # Tipos de datos
    st.write("🧩 **Tipos de Datos por Columna:**")
    st.dataframe(pd.DataFrame(df.dtypes, columns=["Tipo de Dato"]))

    # Datos nulos
    st.write("⚠️ **Cantidad de Valores Nulos por Columna:**")
    nulls = df.isnull().sum()
    st.dataframe(nulls[nulls > 0].to_frame(name="Valores Nulos"))

    if nulls.sum() == 0:
        st.success("✅ No hay valores nulos en el dataset.")

    # Estadísticas descriptivas
    st.subheader("📊 Estadísticas Básicas")
    st.dataframe(df.describe().transpose())

    # Vista previa de los datos
    st.subheader("👁 Vista previa de los datos")
    st.dataframe(df.head(10))

else:
    st.warning("Por favor, carga primero los datos en la página de Inicio.")
