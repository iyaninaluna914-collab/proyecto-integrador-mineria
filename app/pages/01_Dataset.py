import streamlit as st
import pandas as pd

st.title("📁 Dataset")

df = pd.read_csv("data/processed/dataset_limpio.csv")

st.subheader("Vista previa del dataset")
st.dataframe(df.head())

st.subheader("Información general")
st.write(df.info())

st.subheader("Estadísticas descriptivas")
st.write(df.describe())
