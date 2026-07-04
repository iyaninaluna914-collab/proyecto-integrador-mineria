import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="EDA - Análisis Exploratorio",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análisis Exploratorio de Datos (EDA)")

# =========================
# CARGA DE DATOS
# =========================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.normpath(os.path.join(CURRENT_DIR, "..", "data", "processed", "dataset_limpio.csv"))

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    df = pd.read_csv("data/processed/dataset_limpio.csv")

# 🚨 FILTRO CRÍTICO: Limpiamos los datos atípicos de edad de entrada 
# para que afecte correctamente a todos los gráficos siguientes.
df = df[(df["age"] > 0) & (df["age"] <= 90)]

st.write("Vista general del dataset:")
st.dataframe(df.head())

st.divider()

# =========================
# 1. UNIVARIADO - EDAD
# =========================
st.subheader("📌 1. UNIVARIADO - EDAD")

fig1, ax1 = plt.subplots()

# Ahora 'df' ya está limpio, por lo que este histograma saldrá perfecto
df["age"].hist(bins=20, ax=ax1)

ax1.set_title("Distribución de edad")
ax1.set_xlabel("Edad")
ax1.set_ylabel("Frecuencia")

st.pyplot(fig1)

# ... El resto de tu código continúa exactamente igual ...