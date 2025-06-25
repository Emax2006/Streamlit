import streamlit as st
import pandas as pd
from data_manager import get_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

st.title("🚨 Predicción de Probabilidad de Accidentes por Marca")

df = get_data()

if df is not None:
    if 'brand' not in df.columns or 'accidents_reported' not in df.columns:
        st.error("⚠️ El dataset no tiene las columnas necesarias: 'brand' o 'accidents_reported'.")
    else:
        st.markdown("Selecciona **al menos tres marcas** para estimar la **probabilidad de accidente** de los autos.")

        marcas_disponibles = df['brand'].unique().tolist()
        marcas_seleccionadas = st.multiselect("Selecciona marcas", marcas_disponibles)

        if len(marcas_seleccionadas) >= 3:
            df_filtrado = df[df['brand'].isin(marcas_seleccionadas)].copy()
            df_filtrado['accidentado'] = df_filtrado['accidents_reported'].apply(lambda x: 1 if x > 0 else 0)

            # Preprocesar variables numéricas y categóricas
            features = ['engine_cc', 'make_year', 'owner_count', 'mileage_kmpl']
            df_filtrado = df_filtrado.dropna(subset=features + ['brand'])

            # Codificar marca
            le_brand = LabelEncoder()
            df_filtrado['brand_encoded'] = le_brand.fit_transform(df_filtrado['brand'])

            X = df_filtrado[features + ['brand_encoded']]
            y = df_filtrado['accidentado']

            # Entrenar modelo de clasificación
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            model = RandomForestClassifier(random_state=42)
            model.fit(X_train, y_train)

            # Calcular probabilidad promedio por marca
            df_filtrado['prob_accidente'] = model.predict_proba(X)[:, 1]
            prob_por_marca = df_filtrado.groupby('brand')['prob_accidente'].mean().reindex(marcas_seleccionadas)

            st.subheader("📊 Probabilidad promedio de accidente por marca")
            st.dataframe(prob_por_marca.rename("Probabilidad").apply(lambda x: f"{x:.2%}"))

            # Gráfico de barras
            st.subheader("📉 Gráfico de probabilidad de accidentes")
            fig, ax = plt.subplots()
            prob_por_marca.plot(kind='bar', ax=ax, color='salmon')
            ax.set_ylabel("Probabilidad de accidente")
            ax.set_xlabel("Marca")
            ax.set_title("Probabilidad estimada de accidente por marca")
            ax.set_ylim(0, 1)
            st.pyplot(fig)

        elif len(marcas_seleccionadas) > 0:
            st.warning("⚠️ Por favor selecciona **al menos tres marcas** para generar la predicción.")
        else:
            st.info("Selecciona marcas del menú para empezar.")
else:
    st.warning("Por favor, sube primero el archivo en la página de Inicio.")
