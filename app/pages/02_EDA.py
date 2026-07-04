import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="EDA - Análisis Exploratorio",
    page_icon="📊",
    layout="wide"
)

sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.facecolor': 'white', 'axes.facecolor': 'white'})

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("Análisis completo del comportamiento de usuarios a través de variables clave del dataset.")

# =========================
# CARGA DE DATOS
# =========================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "..", "data", "processed", "dataset_limpio.csv")

df = pd.read_csv(DATA_PATH)

# =========================
# LIMPIEZA GENERAL
# =========================
df = df[
    (df["age"] > 0) &
    (df["age"] <= 90) &
    (df["monthly_watch_time_mins"] < 10000)
]

# =========================
# KPI (CORREGIDO)
# =========================
TOTAL_INICIAL = 816
TOTAL_FINAL = 690

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric("📌 Registros Iniciales", TOTAL_INICIAL)

with kpi2:
    st.metric("📌 Registros Finales", TOTAL_FINAL)

with kpi3:
    st.metric("📌 Reducción", f"{TOTAL_INICIAL - TOTAL_FINAL}")

st.divider()

# =========================
# DATA PREVIEW
# =========================
st.subheader("🔍 Vista del dataset")
st.dataframe(df.head())

st.divider()

# =========================
# UNIVARIADO
# =========================
st.header("🎯 Análisis Univariado")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Edad de usuarios")

    fig1, ax1 = plt.subplots(figsize=(6,4))
    df["age"].hist(bins=20, color="#4C72B0", edgecolor="white", ax=ax1)

    ax1.set_title("Distribución de Edad")
    ax1.set_xlabel("Edad")
    ax1.set_ylabel("Frecuencia")

    st.pyplot(fig1)

with col2:
    st.subheader("Planes de suscripción")

    fig2, ax2 = plt.subplots(figsize=(6,4))

    df["subscription_plan"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        colormap="Pastel1",
        ax=ax2
    )

    ax2.set_ylabel("")
    ax2.set_title("Distribución de planes")

    st.pyplot(fig2)

st.divider()

# =========================
# BIVARIADO
# =========================
st.header("🔄 Análisis Bivariado")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Edad vs Uso")

    fig3, ax3 = plt.subplots(figsize=(6,4))

    sns.regplot(
        data=df,
        x="age",
        y="monthly_watch_time_mins",
        scatter_kws={"alpha": 0.4, "color": "#2ECC71"},
        line_kws={"color": "#E74C3C"},
        ax=ax3
    )

    ax3.set_title("Edad vs Uso mensual")
    st.pyplot(fig3)

with col4:
    st.subheader("Edad promedio por género")

    edad_genero = df.groupby("favorite_genre")["age"].mean().sort_values()

    fig4, ax4 = plt.subplots(figsize=(6,4))

    sns.barplot(
        x=edad_genero.index,
        y=edad_genero.values,
        palette="Blues_r",
        ax=ax4
    )

    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
    ax4.set_title("Edad promedio por género")

    st.pyplot(fig4)

st.divider()

# =========================
# MULTIVARIADO
# =========================
st.header("🔮 Análisis Multivariado")

df2 = df.copy()

df2["subscription_plan"] = (
    df2["subscription_plan"]
    .astype(str)
    .str.lower()
    .str.strip()
)

mapeo = {
    "standard": "Standard",
    "std": "Standard",
    "basic": "Basic",
    "basico": "Basic",
    "premium": "Premium",
    "premiun": "Premium",
}

df2["subscription_plan"] = df2["subscription_plan"].map(mapeo).fillna(df2["subscription_plan"])

fig5, ax5 = plt.subplots(figsize=(10,5))

sns.scatterplot(
    data=df2,
    x="age",
    y="monthly_watch_time_mins",
    hue="subscription_plan",
    palette="Set2",
    alpha=0.6,
    ax=ax5
)

sns.regplot(
    data=df2,
    x="age",
    y="monthly_watch_time_mins",
    scatter=False,
    color="black",
    ax=ax5
)

ax5.set_title("Edad vs Uso por Plan")
st.pyplot(fig5)

st.success("✅ EDA finalizado correctamente")
