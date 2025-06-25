import streamlit as st
import pandas as pd

def load_data(data_or_file):
    """Puede recibir un archivo o un DataFrame directamente."""
    if isinstance(data_or_file, pd.DataFrame):
        df = data_or_file
    else:
        df = pd.read_csv(data_or_file)
    st.session_state["data"] = df
    return df

def get_data():
    return st.session_state.get("data", None)
